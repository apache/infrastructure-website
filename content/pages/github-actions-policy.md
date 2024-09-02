Title: GitHub Actions Policy

license: https://www.apache.org/licenses/LICENSE-2.0

This page documents the policies for using [GitHub Actions](github-actions-secrets.html) at the Apache Software Foundation.

For details on the use of requirement level terms, see the <a href="https://www.ietf.org/rfc/rfc2119.txt" target="_blank">requirements levels</a> standard.

### Resource use
Due to misconfigurations in their builds, some projects have been using unsupportable numbers of [GitHub Actions](github-actions-secrets.html). As part of fixing this situation, Infra has established a policy for GitHub Actions use. This section of the policy comes into effect on **April 20, 2024**:

  - All workflows **MUST** have a job concurrency level less than or equal to 20. This means a workflow cannot have more than 20 jobs running at the same time across all matrices.
  - All workflows **SHOULD** have a job concurrency level less than or equal to 15. Just because 20 is the max, doesn't mean you should strive for 20.
  - The average number of minutes a project uses _per calendar week_ **MUST NOT** exceed the equivalent of 25 full-time runners (250,000 minutes, or 4,200 hours).
  - The average number of minutes a project uses _in any consecutive five-day period_ **MUST NOT** exceed the equivalent of 30 full-time runners (216,000 minutes, or 3,600 hours).

Projects whose builds consistently cross the maximum use limits will lose their access to GitHub Actions until they fix their build configurations.

### Triggers

You **MUST NOT** use `pull_request_target` as a trigger on **ANY** action that exports **ANY** confidential credentials or tokens such as `GITHUB_TOKEN` or `NPM_TOKEN`.

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

Projects that have a strong desire to use the “only require approval first time” option should communicate that, explaining their reasons, in a Jira ticket for Infra.

Projects will be allowed to continue using the "only require approval first time" feature, provided they affirm that they will actively monitor their workflows for abuse and act accordingly. Failure to do so may result in the workflow settings being switched back to "always require approval for external contributors".
