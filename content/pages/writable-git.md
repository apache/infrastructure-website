Title: Writable Git repositories

Many Apache projects have moved to Git as their main source code repository since 2012. This option is available to any project, with the following policies in place:

  - We recommend using <a href="https://github.com/apache/" target="_blank">GitHub</a> for your interactions with writable Git repositories. A <a href="http://github.com/apache/" target="_blank">list of those</a> is available.
  - Those who have reservations about GitHub's terms and conditions can use Apache's <a href="https://gitbox.apache.org/" target="_blank">gitbox</a>, which also gives full access to Apache's writable Git repositories.
  - To link your GitHub and Apache IDs, follow <a href="https://gitbox.apache.org/setup/" target="_blank">these instructions</a>.
  - Projects can request new, blank repositories through <a href="https://selfserve.apache.org" target="_blank">selfserve</a>.
  - Apache does not support custom commits or other hooks. All projects get the same hooks. Setting up <a href="https://github.com/apache/infrastructure-puppet/tree/deployment/modules/gitpubsub" target="_blank">gitpubsub</a> should provide sufficient flexibility without impacting the core Git setup. 
