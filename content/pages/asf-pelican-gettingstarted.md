Title: ASF-Pelican getting-started guide

Any ASF project can use the [ASF-Pelican template](asf-pelican.html) as the basis for their project website. 

Review the [Apache Template example](https://template.staged.apache.org/) to see whether the template's features will support the functions you need for your project


## How to use this template

1. Review the <a href="https://github.com/apache/template-site" target="_blank">code repository for ASF-Pelican</a> to confirm that it provides the features your project site needs.

2. Create a <a href="https://issues.apache.org/jira/Jira" target="_blank">Jira ticket</a>, requesting Infra to create a repository using this template for your project. Provide a name and short description for the repository. Infra will confirm the repository's location when it is ready for you.

**Note**: we strongly suggest that you do your site development in a branch rather than the trunk of the repository, and then merge the branch into the trunk when you are sure that everything as working as you would like it. Each commit to the trunk triggers an automatic build to update your live site; this is great for trivial changes like correcting typos, but more of a challenge if you are making major changes and it turns out that there is an error in your code that disables your live site. 

<!--- Review [ASF Pelican feature branches](asf-pelican-branches.html). --->

3. In `theme/apache/templates`, update the theme's `base.html` to fit your site's requirements.

   The example has the following frameworks.

     - JavaScript:
       - [JQuery 3.6.0 Slim](https://code.jquery.com/jquery-3.6.0.slim.js)
       - [Popper 1.14.7](https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.js)
       - [Bootstrap 4.3.1](https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.js)
     - CSS:
       - [Bootstrap 4.3.1](https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.css)
       - [GitHub Markdown 3.0.1](https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/3.0.1/github-markdown.css)

     For fenced code highlighting, review <a href="https://highlightjs.org" target="_blank")>highlightjs</a>.

   - The `content/images` folder holds example logo files. Place your own site's image files here.

4. Determine if your site requires a [data model](https://infra.apache.org/asf-pelican-data.html).

   - The `.ezmd` files in the <a href="https://github.com/apache/template-site/tree/main/content" target="_blank">content</a> directory show examples
   - <a href="https://github.com/apache/template-site/blob/main/asfdata.yaml" target="_blank">asfdata.yaml</a> has many examples
   - Remove the following if you do not need a data model:
     1. `asfdata.yaml`
     2. `data/eccn` directory

5. Edit the `asf.yaml` configuration file:

```
pelican:
  notify: wave@apache.org
  autobuild: preview/*
  target: YOUR SITE'S REPOSITORY
  theme: theme/apache
  whoami: main

staging:
  profile: ~
  whoami: YOUR SITE'S REPOSITORY
  autostage: preview/*
```

6. Update `pelicanconfig.yaml` with your site's information. See [Configuring ASF Pelican](asf-pelican-config.html) for details.

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
