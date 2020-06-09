Title: SVN to Git migration

Migrating your project's code repository from Subversion to Git is now **self-serve**.

  1. Request a bare (empty) Git repository via <a href="https://selfserve.apache.org/" target="_blank">selfserve</a>.
  1. Use <a href="https://github.com/nirvdrum/svn2git">svn2git</a> to convert your SVN repository to Git. 
  1. When the conversion is complete, push the new repository to `gitbox.apache.org` (or GitHub).
  1. Ask Infra (using a Jira ticket) to set the old SVN repository to read-only.

The SVN authors' list (required by svn2git for cloning) is at <a href="https://gitbox.apache.org/authors.txt" target="_blank">https://gitbox.apache.org/authors.txt</a>.

