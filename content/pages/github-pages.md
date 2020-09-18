Title: GitHub Pages for projects

Projects with a Git repository can _in theory_ use <a href="https://pages.github.com/" target="_blank">GitHub Pages</a> to host and deploy the project website. However, Infra does not yet have a complete setup for supporting a project's site from GH Pages. One project has used it successfully as a proof of concept.

The material below is theoretical at this point.

### Using gh-pages for staging a website, product preview, or documentation ###

Projects can use GitHub and gh-pages for staging a website for review and improvement before publishing it to TLP servers.

Ask Infra (in a Jira ticket) to enable 'gh-pages' for your Git repository, and use a 'gh-pages' branch for publishing, or specify a different branch such as 'master' or 'master/docs'.

There are various ways to build and publish your staging site, including:

  - Use Infra's new feature <a href="https://cwiki.apache.org/confluence/display/INFRA/git+-+.asf.yaml+features" target="_kblank">.asf.yaml.</a>
  - Use Buildbot in combination with Jekyll and Pelican
  - Use your own build tool in combination with gh-pages or .asf.yaml

### Using gh-pages for the project website

Projects are welcome to use GitHub for their source code, and to generate (or collect) website pages host and display them at GitHub instead of using the ASF TLP servers.

Ask Infra (in a Jira ticket) to enable 'gh-pages' for the project. When that feature is available, prepare and review your website. When you are happy with its look and functions, change the DNS to point to the site on GitHub.
