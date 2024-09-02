Title: SVN to Git migration

license: https://www.apache.org/licenses/LICENSE-2.0

If your project has an existing SVN mirror on GitHub, and it is up to date, you can request that Infra make the mirror primary/canonical. Open an Infra Jira ticket and include a link to project consensus from your mailing list. Infra will mark your SVN repo as read-only and convert the GitHub mirror to a writable repository.

If your project has an existing SVN mirror on GitHub and it is NOT up to date, please open an Infra Jira ticket to discuss your options.

If you do not have an existing GitHub mirror, you can self-serve your migration using the following steps:

  1. Request a bare (empty) Git repository via <a href="https://selfserve.apache.org/" target="_blank">selfserve</a>.
  1. Use <a href="https://github.com/nirvdrum/svn2git">svn2git</a> to convert your SVN repository to Git. 
  1. When the conversion is complete, push the new repository to `gitbox.apache.org` (or GitHub).
  1. Ask Infra (using a Jira ticket) to set the old SVN repository to read-only.

The SVN authors' list (required by svn2git for cloning) is at <a href="https://gitbox.apache.org/authors.txt" target="_blank">https://gitbox.apache.org/authors.txt</a>.


