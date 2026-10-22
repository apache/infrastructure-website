Title: Optimizing GitHub Actions workflows
license: https://www.apache.org/licenses/LICENSE-2.0

GitHub-hosted runners are a **shared** resource: every ASF project draws on the same pool, so the minutes one project saves shorten the queue for everyone else. The [GitHub Actions Policy](github-actions-policy.html) sets the limits every project must stay within, and [How your project can help](services.html#gha-mitigations) lists the quick wins. This page goes further: it collects the optimizations a PMC can implement in its own workflows, with a worked example for each.

The examples come from <a href="https://github.com/apache/airflow" target="_blank">Apache Airflow</a>, whose CI is one of the largest at the ASF and which has tried most of these techniques. Your project's numbers will differ, but each technique applies to other projects.

Some of the techniques below are **experimental**: Airflow is piloting them now, and this page will be updated as results come in. Treat them as recipes to evaluate, not as recommended defaults.

<h3 id="summary">Summary<a class="headerlink" href="#summary" title="Permanent link">&para;</a></h3>

| Technique | Status | Effect in Airflow |
| --- | --- | --- |
| [Run only the tests a change needs](#selective-tests) | In production | A typical PR runs 30-40 jobs instead of the full 239 (Java projects: [Develocity](#selective-tests-java)) |
| [Use smaller runners for small jobs](#smaller-runners) | In production | Bookkeeping jobs moved off the standard runner queue |
| [Cap open pull requests per contributor](#pr-cap) | In production | 210 PRs from 21 contributors closed in the first pass |
| [Run external contributors' CI in their forks](#fork-ci) | **Experimental** | Expected to cut shared-runner use by about 40% |
| [Self-hosted runners with RunsOn](#runs-on) | **Experimental** | Expected to move at least 40% of the heaviest jobs off shared runners |

<h3 id="selective-tests">Run only the tests a change needs<a class="headerlink" href="#selective-tests" title="Permanent link">&para;</a></h3>

The largest saving usually comes from not running work a change cannot affect. A full Airflow CI run is 239 jobs, but most pull requests run 30-40 jobs or fewer. A first job, "selective checks", looks at which files the pull request changes (plus the event, the target branch and the labels) and computes the smallest set of jobs that still gives confidence in the change. Later jobs read their matrix from that job's outputs. A documentation fix gets the docs build, a change to one provider gets that provider's tests, and a change to core code or to CI itself still gets the full run.

How to start, from simplest to most capable:

- Use <a href="https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onpushpull_requestpull_request_targetpathspaths-ignore" target="_blank">`paths` and `paths-ignore` filters</a> so that whole workflows only run when relevant files change.
- Add a first job that inspects the changed files (`git diff --name-only` against the merge base) and writes a JSON matrix to its outputs. Later jobs use `fromJSON()` on it, and skip themselves when it is empty.
- Make the rules conservative: when in doubt, run more. Run the full suite on pushes to the default branch and on scheduled "canary" builds, so anything a pull request skipped is still caught soon after merge.
- Let maintainers force a full run with a label (Airflow uses `full tests needed`).

Airflow reference: <a href="https://github.com/apache/airflow/blob/main/dev/breeze/doc/ci/04_selective_checks.md" target="_blank">selective checks documentation</a>, including the rules it applies and worked examples.

<h4 id="selective-tests-java">Java projects: use Develocity instead of custom rules<a class="headerlink" href="#selective-tests-java" title="Permanent link">&para;</a></h4>

Maven and Gradle projects do not need to write their own selection logic. The ASF has a sponsored instance of [Gradle Develocity](gradle.html) at <a href="https://develocity.apache.org" target="_blank">develocity.apache.org</a>, available to all projects, and it works with both Maven and Gradle builds:

- **Predictive Test Selection** uses the history of your project's builds to pick the tests a change is likely to affect, and skips the rest. Clay Johnson of Gradle presented it at the <a href="https://cwiki.apache.org/confluence/spaces/INFRA/pages/430408857/Infra+Roundtable+2026-07-01" target="_blank">July 2026 Infra Roundtable</a> (notes and slides on the page). An earlier session, at the <a href="https://cwiki.apache.org/confluence/display/INFRA/Infra+Roundtable+2024-03-06%2C+17%3A00+UTC" target="_blank">March 2024 Roundtable</a>, covered Develocity's test features more broadly.
- **The remote build cache** lets a build reuse the outputs, including test results, of modules whose inputs have not changed since an earlier build, so CI only builds and tests what actually changed.
- **Build scans** show where a build spends its time and which tests are failing or flaky, so you know what to fix first.

For an example, Apache Ozone recently made its Maven test goals cacheable and enabled the Develocity remote build cache (<a href="https://issues.apache.org/jira/browse/HDDS-16940" target="_blank">HDDS-16940</a>). To get started, follow the <a href="https://cwiki.apache.org/confluence/display/INFRA/Project+Onboarding+Instructions+for+Develocity" target="_blank">Project Onboarding Instructions for Develocity</a>, and open an Infra Jira ticket if you run into problems.

Maven projects that do not use Develocity can still skip unchanged modules with the <a href="https://maven.apache.org/extensions/maven-build-cache-extension/" target="_blank">Apache Maven Build Cache Extension</a>. Gradle's own <a href="https://docs.gradle.org/current/userguide/build_cache.html" target="_blank">build cache</a> does the same for Gradle builds.

For other build systems, <a href="https://yetus.apache.org/" target="_blank">Apache Yetus</a> can work out which modules a patch touches and test only those.

<h3 id="smaller-runners">Use smaller runners for small jobs<a class="headerlink" href="#smaller-runners" title="Permanent link">&para;</a></h3>

Many jobs do very little work: computing a matrix, posting a notification, labelling or closing issues, checking a file name. They do not need a full `ubuntu-latest` (or `ubuntu-24.04`, `ubuntu-22.04`) virtual machine. Run them on `runs-on: ubuntu-slim`, a much smaller runner type that GitHub schedules from a separate pool, so these jobs start faster at peak times and leave the standard runners for jobs that need them.

`ubuntu-slim` has significant limits, so check a job against them before you move it:

- 1 vCPU and 5 GB of memory, and a small disk.
- A **15-minute** maximum run time.
- It is an unprivileged container, not a VM: there is no Docker daemon, so the job cannot build images, start containers or use Docker container actions.
- A minimal toolset. `actions/setup-*` actions work, but the system Python is externally managed, so a bare `pip install` fails.

A good rule: if a job only moves metadata around, it belongs on `ubuntu-slim`. If it builds, runs containers, or runs a real test suite, keep it on a standard runner. See GitHub's <a href="https://docs.github.com/en/actions/reference/runners/github-hosted-runners" target="_blank">GitHub-hosted runners reference</a> for the current specification.

Airflow reference: <a href="https://github.com/apache/airflow/pull/72852" target="_blank">apache/airflow#72852</a> moved its short CI bookkeeping jobs to `ubuntu-slim`. The <a href="https://github.com/apache/airflow/blob/main/dev/breeze/doc/ci/05_workflows.md#runners" target="_blank">runners section of its CI documentation</a> explains which jobs go where.

<h3 id="pr-cap">Cap open pull requests per contributor<a class="headerlink" href="#pr-cap" title="Permanent link">&para;</a></h3>

Every pull request costs a CI run on every push. Some contributors, often using AI tools, open dozens of low-value pull requests at once, and each one keeps drawing on the shared runners. Airflow had contributors with 30 open pull requests at the same time.

You can cap the number of pull requests a user **without write access** may have open in a repository with the `creation_cap` setting in `.asf.yaml`. Committers and other users with write access are not affected. See <a href="https://github.com/apache/infrastructure-asfyaml/blob/main/README.md#pr_creation_cap" target="_blank">Pull request creation cap</a> in the `.asf.yaml` reference for details.

```yaml
github:
  pull_requests:
    creation_cap:
      enabled: true
      max_open_pull_requests: 5
```

Airflow agreed a cap of 5 by lazy consensus on its dev list. When it enabled the cap it closed the excess pull requests in a one-time pass: 210 pull requests from 21 contributors. Each closed pull request got a comment asking its author to choose which ones matter most and bring those back. Tell your contributors before you enable the cap, and document what they should do when they reach it.

Airflow references: <a href="https://github.com/apache/airflow/pull/73469" target="_blank">apache/airflow#73469</a> (the cap), the <a href="https://github.com/apache/airflow/blob/main/contributing-docs/32_open_pull_request_limit.rst" target="_blank">contributor guide for the limit</a>, and the <a href="https://lists.apache.org/thread/pbry9otfdbkr1n85scq3v9mdlp15fgg2" target="_blank">announcement on the dev list</a>.

<h3 id="fork-ci">Run external contributors' CI in their forks (experimental)<a class="headerlink" href="#fork-ci" title="Permanent link">&para;</a></h3>

**Status: experimental.** Airflow has accepted this design and is starting an opt-in pilot. Findings and reusable recipes will be published here when the pilot ends.

A fork has its own GitHub Actions quota. When a pull request comes from a contributor without write access, its CI can run in the contributor's fork instead of on the ASF's shared runners. In Airflow's design ("your PR, your CI"):

- CI for a pull request from an external contributor runs in their fork. The pull request shows the fork run's status and links to it.
- The pull request stays in draft until its fork run passes, so maintainers mostly review pull requests that already pass.
- Committers' and collaborators' pull requests keep using project CI as before.
- A passing fork run is trusted only when the pull request does not change what CI runs (`.github/`, the CI tooling and scripts). Such pull requests stay in draft until a maintainer reviews them and runs project CI with a label. Maintainers can use the same label on any pull request they want verified in project CI before merging.
- The gate never falls back to project CI when it cannot decide, and a pull request that edits the workflows to get around the gate is detected and closed.

Airflow expects this to cut its use of shared runners by about 40%.

Airflow references: <a href="https://cwiki.apache.org/confluence/spaces/AIRFLOW/pages/451974711/AIP-120+Run+CI+for+external+contributions+in+contributor+forks" target="_blank">AIP-120: Run CI for external contributions in contributor forks</a>, the design and ADR in <a href="https://github.com/apache/airflow/pull/73378" target="_blank">apache/airflow#73378</a>, and the implementation, which starts with <a href="https://github.com/apache/airflow/pull/74819" target="_blank">apache/airflow#74819</a> (the gate), <a href="https://github.com/apache/airflow/pull/74820" target="_blank">#74820</a> (fork-mode selective checks) and <a href="https://github.com/apache/airflow/pull/74822" target="_blank">#74822</a> (reconciler).

<h3 id="runs-on">Self-hosted runners with RunsOn (experimental)<a class="headerlink" href="#runs-on" title="Permanent link">&para;</a></h3>

**Status: experimental.** Airflow's proposal has been called for lazy consensus and its implementation is under review. This section will be updated with results once it is in use.

If your project has cloud credits, for example from a targeted donation, you can move its heaviest jobs off the shared runners. <a href="https://runs-on.com" target="_blank">RunsOn</a> starts an ephemeral EC2 instance in **your project's own AWS account** for each job, while GitHub Actions remains the orchestrator. A workflow requests one with a `runs-on:` label that names the size it needs, for example `runs-on=${{ github.run_id }}/cpu=8/ram=32`. There is no cluster to operate, both AMD and ARM instances are available, and RunsOn offers a free license to open source projects in exchange for a public acknowledgement. Apache Arrow, Apache DataFusion and ASF Infra already use it.

Self-hosted runners need Infra's involvement: read [Self-hosted runners](self-hosted-runners.html) and open an Infra Jira ticket before you start.

In Airflow's design, the AWS account is funded by AWS Open Source credits granted for this purpose:

- Scheduled canary runs and pushes to `apache/airflow` branches run on RunsOn, and so do pull requests from `apache/airflow` branches.
- Pull requests from forks stay on GitHub-hosted runners, with a read-only token and no secrets, as before. A committer can opt a fork pull request in with a label.
- Any pull request can be sent back to GitHub-hosted runners with a label, and a repository variable moves every run back without a code change, for when RunsOn or the budget is unavailable.
- Windows jobs stay on GitHub-hosted runners.
- Self-hosted runners do not become the default for all pull requests until the budget is known to support it.

Airflow expects this to move at least 40% of its heaviest jobs (the complete and full test runs) off the shared runners.

<h4 id="runs-on-security">Securing self-hosted runners<a class="headerlink" href="#runs-on-security" title="Permanent link">&para;</a></h4>

A self-hosted runner gives every job that lands on it compute in your cloud account and whatever that account lets the instance reach. The review of Airflow's implementation found the following. Address each item before you let pull requests run on self-hosted runners.

- **The workflow's choice of runner is not a security boundary.** A `pull_request` run uses the workflow files and scripts from the pull request itself. Whatever logic your workflow uses to decide which jobs go to self-hosted runners, a pull request from a fork can change it, or put a RunsOn label in `runs-on:` directly and ask for any instance size. Treat that logic as a routing preference. The restriction has to be enforced outside the repository, in the RunsOn stack and the cloud account.
- **Approval for fork workflows does not close the gap.** Even "Require approval for all external contributors" exempts members of the `apache` GitHub organization (committers of any ASF project who linked their GitHub account) and the repository's collaborators. Ask Infra to confirm your repository's approval setting, but do not rely on it.
- **Restrict what the instance can reach.** Limit the instance role to the cache bucket prefix the jobs need, with no access to RunsOn's configuration bucket. Deny network traffic between runners in the security group, because CI jobs often bind unauthenticated local services on all interfaces. Disable SSH access, and isolate sticky disks between jobs (`EnableStickyDiskIsolation`).
- **Cap cost in the stack, not just in alerts.** Limit the instance types jobs can request and their run time (`RunnerMaxRuntime`). RunsOn has no instance cap of its own, and its daily budget setting (`AppBudgetDailyUsd`) only alerts, so use the account's EC2 vCPU quotas as the hard ceiling. Airflow has a separate proposal, AIP-119, for anomaly monitoring and guardrails in its AWS account.
- **Consider a separate stack for untrusted code.** Running pull requests from forks on their own stack, in their own account or with a role that can reach nothing beyond its own cache bucket, is stronger than sharing a stack with the jobs that hold secrets.
- **Bind an opt-in label to the reviewed commit.** A label that sends a fork pull request to self-hosted runners would otherwise also cover every later push. Airflow honours the label only while a committer's latest review approves the pull request's current head commit and no committer's request for changes stands. A re-run reuses the labels of its original event, so check the pull request's current labels through the API rather than the event payload.
- **Make shared caches tamper-evident.** Every job on the stack can write to the cache bucket, so a pull request's job could overwrite a cached artifact that a later job with secrets restores. Name cached blobs by their SHA-256 digest, store the digest through a store the job cannot forge (Airflow uses the ASF stash action, whose restore accepts only artifacts from the same run or branch), and verify the digest before extracting. A tampered blob then only causes a cache miss.
- **Keep a way back.** A repository variable that sends every run back to GitHub-hosted runners lets you switch off self-hosted runners quickly if the stack or the credits lapse.

RunsOn offers two modes. Fleet adds a GitHub runner group restricted to selected workflows, but GitHub matches those workflows by ref, so runs of a pull request (`refs/pull/N/merge`) never qualify, and Fleet then covers only canary and push runs. Airflow chose Flex on a hardened stack, as described above, which is also how Infra already runs RunsOn for pull requests in other ASF repositories.

Airflow references: <a href="https://cwiki.apache.org/confluence/x/-JXwGg" target="_blank">AIP-118: Self-hosted runners for Apache Airflow CI</a> and its <a href="https://cwiki.apache.org/confluence/spaces/AIRFLOW/pages/451974672/AIP-118+Appendix+%E2%80%94+evidence+and+implementation+details" target="_blank">appendix with evidence and implementation details</a>, the <a href="https://lists.apache.org/thread/t6cr2gnmnxk3pczoklm954zzy2wcn98d" target="_blank">AIP-119 discussion</a> on cost guardrails, the implementation and its security review in <a href="https://github.com/apache/airflow/pull/74889" target="_blank">apache/airflow#74889</a>, and the earlier full-CI experiment in <a href="https://github.com/apache/airflow/pull/74714" target="_blank">apache/airflow#74714</a>. See also RunsOn's own <a href="https://runs-on.com" target="_blank">documentation</a> on security for public repositories.

<h3 id="help">Getting help<a class="headerlink" href="#help" title="Permanent link">&para;</a></h3>

If you want advice on which of these fits your project, or you have optimizations of your own that worked, contact Infra via a Jira ticket or by email to `users@infra.apache.org`. We will add proven recipes from other projects to this page.
