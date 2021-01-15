Title: GitHub Actions Policy

This page documents the policies for using [GitHub Actions](github-actions-secrets.html) at the Apache Software Foundation.

For details on the use of requirement level terms, see the <a href="https://www.ietf.org/rfc/rfc2119.txt" target="_blank">requirements levels</a> standard.

### Triggers: ###

You **MUST NOT** use `pull_request_target` as a trigger on **ANY** action that exports **ANY** confidential credentials or tokens such as `GITHUB_TOKEN` or `NPM_TOKEN`.

### External actions ###

You **MAY** use all actions internal to the `apache/*`, `github/*` and `actions/*` namespaces without restrictions.

You **MUST** pin all external actions to the specific git hash (SHA1) of the action that has been reviewed for use by the project. For instance, you **MUST** pin `foobar/baz-action@8843d7f92416211de9ebb963ff4ce28125932878`.


### Pushing commits to repositories###

In general, only committers **MAY** push commits to repositories.

Automated services such as GitHub Actions (and Jenkins, BuildBot, etc.) **MAY** work on website content and other non-released data such as documentation and convenience binaries.
Automated services **MUST NOT** push data to a repository or branch that is subject to official release as a software package by the project, **unless** the project secures specific prior authorization of the workflow from Infrastructure.
