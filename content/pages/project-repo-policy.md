Title: Project Code Repository Policy

Apache projects can have Subversion or Git code repositories for their product code and assets. The majority of projects now use Git.

  - Projects can have as many **public repositories** as their work requires.
  - Each project can also request (using a Jira ticket) that Infra set up **one private Git repository** for use with tasks, such as fixing security issues in project code, that should not be publicly available. The PMC must explain its need of a private repo in a Jira ticket for Infa. Only members of the project's PMC can see this repository or read its contents.
    - Private repos **must** have commit/PR/issues emails sent to the project's `private@` list.  

### Git Repos

  1. We recommend using <a href="https://github.com/apache/" target="_blank">GitHub</a> for your interactions with <a href="http://github.com/apache/" target="_blank">writable Git repositories</a>.
  1. Those who have reservations about GitHub's terms and conditions can use Apache's <a href="https://gitbox.apache.org/" target="_blank">GitBox</a>, which also gives full access to Apache's writable Git repositories.
  1. To link your GitHub and Apache IDs, follow <a href="https://gitbox.apache.org/setup/" target="_blank">these instructions</a>.
  1. Projects can request new, blank, public repositories through <a href="https://selfserve.apache.org" target="_blank">selfserve</a>.
  1. Apache does not support custom commits or other hooks. All projects get the same hooks. Setting up <a href="https://github.com/apache/infrastructure-puppet/tree/deployment/modules/gitpubsub" target="_blank">gitpubsub</a> should provide sufficient flexibility without impacting the core Git setup. 

### Subversion Repos

You can find Subversion repos at <a href="https://svn.apache.org/viewvc" target="_blank">svn.apache.org/viewvc</a>.

### Repository Access

  1. ASF projects are required to house their project code in ASF supported services (Subversion, GitBox).
  1. Only people with an ICLA on file with Apache can create, edit, or update code housed within the ASF. There is no third-party access to create, edit, or delete files.
  1. Apache software projects are open-source, so everyone has **read** access to all public code housed within the ASF.
  1. Documentation is not code. Projects can host their documentation anywhere (such as on platforms like readthedocs and gitlab) and, if they choose, make them available to the world to create and edit pages.
  1. However, if projects create and house their documentation inside the ASF, statement 2 applies to it.

Since the primary presence of an Apache project must be within Apache, there is an argument for storing project documentation in its own repository alongside the project's code repository. This practice also makes it easier for project committers to move from committing new features, or updates to existing features, to writing about them for the project's users.
