Title: Writable Git repositories

Many Apache projects have moved to Git as their main source code repository since 2012. This option is available to any project, with the following policies in place:

  - <a href="https://gitbox.apache.org/" target="_blank">gitbox</a> is the entry point for writable Git repositories. A <a href="https://gitbox.apache.org/repos/asf" target="_blank">list of those</a> is available.
  - To link your GitHub and Apache ID follow <a href="https://gitbox.apache.org/setup/" target="_blank">these instructions</a>.
  - Feel free to use <a href="https://gitbox.apache.org/" target="_blank">gitbox</a> or <a href="https://github.com/apache/" target="_blank">github</a> as your upstream origin.
  - Projects can request new, blank repositories through <a href="https://selfserve.apache.org" target="_blank">selfserve</a>.
  - Apache does not support custom commits or other hooks. All projects get the same hooks. Setting up <a href="https://github.com/apache/infrastructure-puppet/tree/deployment/modules/gitpubsub" target="_blank">gitpubsub</a> should provide sufficient flexibility without impacting the core Git setup. 
