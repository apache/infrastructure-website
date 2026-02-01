Title: GitHub Pages for projects 
license: https://www.apache.org/licenses/LICENSE-2.0

Projects with a Git repository can use <a href="https://pages.github.com/" target="_blank">GitHub Pages</a> (gh-pages) to host and deploy the project website. 

### Using gh-pages for staging a website, product preview, or documentation

Projects can use GitHub and gh-pages for staging a website for review and improvement before publishing it to TLP servers.

See <a href="https://github.com/apache/infrastructure-asfyaml/blob/main/README.md#pages" target="_blank">this section on the Infra wiki page about asf.yaml</a> for how to enable gh-pages for your Git repository.

There are various ways to build and publish your staging site, including:

  - Use Infra's <a href="https://github.com/apache/infrastructure-asfyaml/blob/main/README.md" target="_blank">.asf.yaml.</a>
  - Use Buildbot in combination with Jekyll and Pelican
  - Use your own build tool in combination with gh-pages or .asf.yaml

### Using gh-pages for the project website

Projects are welcome to use GitHub for their source code, and to generate (or collect) website pages host and display them at GitHub instead of using the ASF TLP servers.

See <a href="https://github.com/apache/infrastructure-asfyaml/blob/main/README.md#pages">this section on the Infra wiki page about asf.yaml</a> for how to enable gh-pages for your Git repository. Then prepare and review your website. When you are happy with its look and functions, change the DNS to point to the site on GitHub.
