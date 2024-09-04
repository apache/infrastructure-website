title: Policy on use of GitHub Actions
license: https://www.apache.org/licenses/LICENSE-2.0

Due to misconfigurations in their builds, some projects have been using unsupportable numbers of [GitHub Actions](github-actions-secrets.html). As part of fixing this situation, Infra has established a policy for GitHub Actions use. This policy comes into effect on **April 20, 2024**:

  - All workflows **MUST** have a job concurrency level less than or equal to 20. This means a workflow cannot have more than 20 jobs running at the same time across all matrices.
  - All workflows **SHOULD** have a job concurrency level less than or equal to 15. Just because 20 is the max, doesn't mean you should strive for 20.
  - Workflows **MUST NOT** use `pull_request_target` in a workflow without prior consent from Infra.
  - The average number of minutes a project uses _per calendar week_ **MUST NOT** exceed the equivalent of 25 full-time runners (250,000 minutes, or 4,200 hours).
  - The average number of minutes a project uses _in any consecutive five-day period_ **MUST NOT** exceed the equivalent of 30 full-time runners (216,000 minutes, or 3,600 hours).

Projects whose builds consistently cross the maximum use limits will lose their access to GitHub Actions until they fix their build configurations.
