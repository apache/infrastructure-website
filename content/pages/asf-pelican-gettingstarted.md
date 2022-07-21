Title: ASF-Pelican getting-started guide

Any ASF project using a Git repository can use the [ASF-Pelican template](asf-pelican.html) as the basis for their project website. 

Review the [Apache Template example](https://template.staged.apache.org/) to see whether the template's features will support the functions you need for your project.


## How to use this template

First, review the <a href="https://github.com/apache/template-site" target="_blank">code repository for ASF-Pelican</a> to confirm that it provides the features your project site needs. The template builds a copy of the full Apaches Software Foundation website, which has features your site does not need, and lacks features, such as a download page for product releases, that you will need to add. (During the summer of 2022 we will update the template contents to better reflect the features a project website should have.



If you wish to try out the template:

  1. Using <a href="https://selfserve.apache.org/" target="_blank"self-serve</a>, create a new repo for the code and resources for your project’s website.
  2. Clone the empty repo to a location on your computer.
  3. Download the <a href="https://github.com/apache/infrastructure-website/archive/refs/heads/master.zip">template zipfile</a>.
  4. Unzip `master.zip` and copy `infrastructure-website-master/*`  to the root of your new repository.
  5. Configure <a href="https://cwiki.apache.org/confluence/display/INFRA/Git+-+.asf.yaml+features" target="_blank">.asf.yaml</a>:

```
pelican:
  notify: EMAIL of a person on your team to receive error messages related to Pelican
  autobuild: preview/*
  target: YOUR SITE'S REPOSITORY
  theme: theme/apache
  whoami: main

staging:
  profile: ~
  whoami: YOUR SITE'S REPOSITORY
  autostage: preview/*
```

  6. Configure <a href="https://infra.apache.org/asf-pelican-config.html" target="_blank">pelicanconf.yaml</a>.
  7. Commit and push your new website repository. This should trigger the automatic build to staging (`REPONAME.staged.apache.org`).
  8. Review the site to confirm that the template materials display and function correctly.
  9. Add your own content, updating, replacing, and removing template content elements as appropriate. With each commit / push of content, visit the staging site to confirm that the site displays as you expect it to.
  10. If you want to work on and test the site offline, see <a href="https://github.com/apache/infrastructure-website/blob/master/content/pages/asf-pelican-local.html" target="_blank">Local builds of your Pelican-template website</a>.
  11. <a href="https://infra.apache.org/asf-pelican-theme.html" target="_blank">Adjust the theme</a> by editing `base.html` and making any other style changes that will help the site present your projectg and product well. Don't forget to provide your product's logo in the `content/images` folder.
  12. When you are ready to publish the site, create a pull request to merge the content in staging into the trunk of the repo. That will trigger a build of the live site.
  13. Visit `YourProject.apache.org` after every update to make sure it displays and functions correctly.

**Note**: we strongly suggest that you do your site development in a branch rather than the trunk of the repository, and then merge the branch into the trunk when you are sure that everything as working as you would like it. Each commit to the trunk triggers an automatic build to update your live site; this is great for trivial changes like correcting typos, but more of a challenge if you are making major changes and it turns out that there is an error in your code that disables your live site. 

### Frameworks

The example has the following frameworks.

     - JavaScript:
       - [JQuery 3.6.0 Slim](https://code.jquery.com/jquery-3.6.0.slim.js)
       - [Popper 1.14.7](https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.js)
       - [Bootstrap 4.3.1](https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.js)
     - CSS:
       - [Bootstrap 4.3.1](https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.css)
       - [GitHub Markdown 3.0.1](https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/3.0.1/github-markdown.css)

For fenced code highlighting, consider <a href="https://highlightjs.org" target="_blank">highlightjs</a>.

### Data model

Determine whether your site requires a [data model](https://infra.apache.org/asf-pelican-data.html).

The `.ezmd` files in the template's `content` directory show examples,

<a href="https://github.com/apache/template-site/blob/main/asfdata.yaml" target="_blank">asfdata.yaml</a> has many examples.

Remove the following if you do not need a data model:
  - `asfdata.yaml`
  - `data/eccn` directory


7. Create your [content](content) 

   - `.md` files using Github Flavored Markdown ([**gfm**](https://infra.apache.org/gfm.html))
   - `.ezmd` files for templates using `ASF_DATA`

8. Building

   - [Local build instructions](https://infra.apache.org/asf-pelican-local.html)
   - [ASF YAML build](.asf.yaml) -- ASF infrastructure instructions

9. When you are ready to use this repository as the source for your live site, create a Jira ticket to ask Infra to adjust the build process. From then on, changes you make to the trunk of this repository automatically update the live site.

## Issues and template questions

Please let us know if you run into issues with the template.

   - [Issues](https://github.com/apache/template-site/issues)

## Earlier versions

Earlier versions of this template made use of a `pelicanconf.py` configuration file. The current version uses `.asf.yaml` and `pelicanconf.yaml`, as noted above. We retain the earlier instruction for the projects using the earlier version of the template; however, any project starting with the template now should use the files and instructions noted above.

```
 Edit the `pelicanconf.py` configuration file:

   - Website specific
   - `PLUGINS`
   - `ASF_DATA` - `asfdata.py` plugin settings
   - `ASF_GENID` - `asfgenid.py` plugin settings
     `asfgenid.py` performs a series of html fixups including permalinks, heading ids, and table of contents
```

# EZMD format

The [EZMD](https://infra.apache.org/asf-pelican-build.html#ezmd) format is a markdown extension of [EZT](https://github.com/gstein/ezt/blob/wiki/Syntax.md). 
It allows for embedding ezt inside markdown with modifications so simplify the process of fetching generated/external data.
