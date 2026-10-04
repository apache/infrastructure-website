Title: GitHub Actions Policy
license: https://www.apache.org/licenses/LICENSE-2.0

This page documents the policies for using [GitHub Actions](github-actions-secrets.html) at the Apache Software Foundation.

For details on the use of requirement level terms, see the <a href="https://www.ietf.org/rfc/rfc2119.txt" target="_blank">requirements levels</a> standard.

For additional advice on how to use this feature safely, see <a href="https://cwiki.apache.org/confluence/display/BUILDS/GitHub+Actions+Security" target="_blank">GitHub Actions Security</a>.

### Dependabot
All repositories using GitHub Actions **must** have automatic dependency management in place using one of these tools:
* <a href="https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide" target="_blank">GitHub Dependabot</a> for the <a href="https://docs.github.com/en/code-security/reference/supply-chain-security/supported-ecosystems-and-repositories#github-actions" target="_blank">`github-actions` ecosystem</a>
* <a href="https://docs.renovatebot.com/getting-started/running/#forking-renovate-app" target="_blank">Forking Renovate</a> using the <a href="https://docs.renovatebot.com/modules/manager/github-actions/" target="_blank">GitHub actions manager</a>

See the [Dependabot](dependabot.html) page for how to configure it, including [grouping security updates](dependabot.html#group-security-updates) so that a burst of advisories does not turn into a burst of CI runs.
 
### Resource use
Due to misconfigurations in their builds, some projects have been using unsupportable numbers of [GitHub Actions](github-actions-secrets.html). As part of fixing this situation, Infra has established a policy for GitHub Actions use:

  - All workflows **MUST** have a job concurrency level less than or equal to 20. This means a workflow cannot have more than 20 jobs running at the same time across all matrices.
  - All workflows **SHOULD** have a job concurrency level less than or equal to 15. Just because 20 is the max, doesn't mean you should strive for 20.
  - The average number of minutes a project uses _per calendar week_ **MUST NOT** exceed the equivalent of 25 full-time runners (250,000 minutes, or 4,200 hours).
  - The average number of minutes a project uses _in any consecutive five-day period_ **MUST NOT** exceed the equivalent of 30 full-time runners (216,000 minutes, or 3,600 hours).

Projects whose builds consistently cross the maximum use limits will lose their access to GitHub Actions until they fix their build configurations.

**Note**: Projects should review these recommended practices from Git: <a href="https://cwiki.apache.org/confluence/spaces/INFRA/pages/430408443/GitHub+Actions+Recommended+Practices" target="_blank">cwiki.apache.org/confluence/spaces/INFRA/pages/430408443/GitHub+Actions+Recommended+Practices</a>.

Runners are a shared resource, so a project can slow every other project down while staying inside these limits. For why queues build up and what your project can do to reduce its share of the load, see [GitHub Actions](services.html#github-actions) on the Services and Tools page.

### Avoid using the 'pull_request_target' trigger

You **MUST NOT** use `pull_request_target` as a trigger on **ANY** action that exports **ANY** confidential credentials or tokens such as `GITHUB_TOKEN` or `NPM_TOKEN`. An explantion of the risks related to this trigger, and the very limited circumstances in which it may be used, is at <a href="https://cwiki.apache.org/confluence/display/INFRA/GHA-dangers+of+pull_request_target" target="_blank">/cwiki.apache.org/confluence/display/INFRA/GHA-dangers+of+pull_request_target</a>.

#### A safer replacement for `pull_request_target`

From November 2026, the `pull_request_target` trigger is disabled for ASF repositories. Projects still using it should migrate to the pattern below.

Projects have used `pull_request_target` for jobs that need write access in response to a pull request from a fork: commenting on the pull request, labelling it, or publishing something built from it (a website preview, a test report, a coverage summary). You can do all of these without `pull_request_target` by splitting the work across three workflows so that no privileged job ever runs, or even sees, code from the pull request.

1. **Build in `pull_request`, and only produce artifacts.** The existing CI workflow runs on `pull_request`. It runs the pull request's code with a read-only token and no secrets, and uploads whatever the privileged step needs (a built site, a report, a JSON summary) with `actions/upload-artifact`. It does nothing else.
2. **Add a "signal" workflow for events that do not start a build.** If the privileged step must also react to events such as a label being added or a pull request being closed, add a small `pull_request` workflow that does nothing. It has `permissions: {}`, checks nothing out and runs one `echo`. Its only purpose is to complete, which tells the privileged workflow that something happened to a pull request.
3. **Do the privileged work in `workflow_run`**, which starts when the build workflow or the signal workflow completes. GitHub always runs `workflow_run` from the **default branch**, so its code is your reviewed code, never the contributor's. This workflow may hold a write token. It downloads the artifacts produced by the build and comments, labels or publishes.

The signal workflow:

```yaml
name: "PR signal"
on:
  pull_request:
    types: [opened, reopened, labeled, unlabeled, closed]
permissions: {}
jobs:
  signal:
    runs-on: ubuntu-latest
    steps:
      - run: echo "pr-privileged.yml runs when this workflow completes"
```

The privileged workflow:

```yaml
name: "PR privileged actions"
on:
  workflow_run:
    workflows: ["CI", "PR signal"]   # name the workflows explicitly
    types: [completed]
permissions: {}
jobs:
  act:
    if: github.event.workflow_run.event == 'pull_request'
    runs-on: ubuntu-latest
    permissions:
      actions: read          # download the build's artifacts
      pull-requests: write   # comment on and label pull requests
    steps:
      - uses: actions/checkout@<sha>   # the default branch, never the PR
        with:
          persist-credentials: false
      - run: ./scripts/pr-privileged.sh   # from the default branch
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          RUN_ID: ${{ github.event.workflow_run.id }}
```

The pattern is safer because the privileged workflow never relies on the code of the pull request. It receives no checkout, no scripts and no build steps from it; only data. You never need to review the build workflow, which may be large and changes in every pull request, to know what the privileged job will do; you only need to review a small workflow and script on the default branch.

When using this pattern you **MUST** follow these rules:

* Never check out, build or execute code from the pull request in the `workflow_run` workflow. Check out the default branch only.
* Treat the downloaded artifacts as untrusted data, not code. Never execute them, `source` them or install them. Validate their contents (expected files, sizes, formats) before using them, and extract them outside the workspace so they cannot overwrite your scripts.
* Never interpolate values from the triggering event, such as `${{ github.event.workflow_run.head_branch }}`, a pull request title or a comment body, into a `run:` block. Pass only IDs (the run ID, a pull request number) and derive everything else from the GitHub API.
* List the triggering workflows explicitly in `workflows:` and check `github.event.workflow_run.event == 'pull_request'`.
* Set `permissions: {}` at the top level and grant each job only the scopes it needs.

A complete example that publishes website previews of pull requests, including from forks, is in the Apache Magpie website repository:

* <a href="https://github.com/apache/magpie-site/blob/main/.github/workflows/build.yml" target="_blank">build.yml</a>: builds the site and uploads it as an artifact
* <a href="https://github.com/apache/magpie-site/blob/main/.github/workflows/preview-signal.yml" target="_blank">preview-signal.yml</a>: the signal workflow
* <a href="https://github.com/apache/magpie-site/blob/main/.github/workflows/preview-publish.yml" target="_blank">preview-publish.yml</a>: the privileged workflow that publishes the preview

### External actions

You **MAY** use all actions internal to the `apache/*`, `github/*` and `actions/*` namespaces without restrictions.

You **MUST** pin all external actions to the specific git hash (SHA1) of the action that has been reviewed for use by the project. For instance, you **MUST** pin `foobar/baz-action@8843d7f92416211de9ebb963ff4ce28125932878`.

### Using self-hosted runners with GitHub Actions

See this guidance on <a href="https://cwiki.apache.org/confluence/display/INFRA/GitHub+-+self-hosted+runners" target="_blank">GitHub - self-hosted runners</a>.

### Pushing commits to repositories

In general, only committers **MAY** push commits to repositories.

Automated services such as GitHub Actions (and Jenkins, BuildBot, etc.) **MAY** work on website content and other non-released data such as documentation and convenience binaries.
Automated services **MUST NOT** push data to a repository or branch that is subject to official release as a software package by the project, **unless** the project secures specific prior authorization of the workflow from Infrastructure.

### Non-committer contributors and GitHub Actions

GitHub provides an option to allow a non-committer contributor to use GitHub Actions if a previous pull request by that person has been approved. This raises security concerns, and could cause issues with overall use of GitHub Actions. 

The default for this option is to “always require approval for external contributors”.

Projects that have a strong desire to use the “only require approval first time” option should open a Jira ticket with Infra and provide the following information:

* The name(s) of the repo(s) concerned.

* A link to a mailing list discussion showing a consensus vote by the PMC noting, that they affirm that they will actively monitor their workflows for abuse, and that they will act accordingly if and when abuse is detected. Failure to carry out such monitoring and addressing of abuse may result in the workflow settings being switched back to "always require approval for external contributors".

### Details on submitting a GitHub Action for approval
The README file at <a href="https://github.com/apache/infrastructure-actions" target="_blank">github.com/apache/infrastructure-actions</a> has a detailed guide for how to add or update a GitHub Action.
