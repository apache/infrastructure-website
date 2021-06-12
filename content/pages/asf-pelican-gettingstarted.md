Title: ASF-Pelican getting-started guide

Any ASF project can use the [ASF-Pelican template](asf-pelican.html) as the basis for their project website. 

Review the [Apache Template example](https://template.staged.apache.org/) to see whether the template's features will support the functions you need for your project


## How to use this template

**Note: this information is evolving. Please contact Infra if you would like to use the template immediately, as some of the directions below are no longer correct.**

1. Review the <a href="https://github.com/apache/template-site" target="_blank">code repository for ASF-Pelican</a> to confirm that it may provide the features your project site needs.

2. Create a <a href="https://issues.apache.org/jira/Jira" target="_blank">Jira ticket for Infra</a>, requesting Infra to create a repository using this template for your project. Provide a name and short description for the repository. Infra will confirm the repository's location when it is ready for you.

3. **Note**: we strongly suggest that you do your site development in a branch rather than the trunk of the repository, and then merge the branch into the trunk when you are sure that everything as working as you would like it. Each commit to the trunk triggers an automatic build to update your live site; this is great for trivial changes like correcting typos, but more of a challenge if you are making major changes and it turns out that there is an error in your code that disables your live site. 

   Review [ASF Pelican feature branches](asf-pelican-branches.html).

4. In `theme/apache/templates`, update the theme's `base.html` to fit your site's requirements.

   The example has the following frameworks.

     - JavaScript:
       - [JQuery 3.6.0 Slim](https://code.jquery.com/jquery-3.6.0.slim.js)
       - [Popper 1.14.7](https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.js)
       - [Bootstrap 4.3.1](https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.js)
     - CSS:
       - [Bootstrap 4.3.1](https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.css)
       - [GitHub Markdown 3.0.1](https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/3.0.1/github-markdown.css)

     For fenced code highlighting, have a look at [highlightjs](https://highlightjs.org).

   - The `content/images` folder holds example logo files. Place your other site image files here.

5. Determine if your site requires a [data model](https://infra.apache.org/asf-pelican-data.html).

   - The `.ezmd` files in the [content](content) directory show examples
   - [`asfdata.yaml`](asfdata.yaml) has manuy examples
   - Remove the following if you do not need a data model:
     1. `asfdata.py` and `asfreader.py` [Plugins](/theme/plugins)
     2. `asfdata.yaml`
     3. `data` directory

6. Edit your [configuration](pelicanconf.py)

   - Website specific
   - `PLUGINS`
   - `ASF_DATA` - `asfdata.py` plugin settings
   - `ASF_GENID` - `asfgenid.py` plugin settings
     `asfgenid.py` performs a series of html fixups including permalinks, heading ids, and table of contents

7. Create your [content](content)

   - `.md` files using Github Flavored Markdown ([**gfm**](https://infra.apache.org/gfm.html)
   - `.ezmd` files for templates using `ASF_DATA`

8. Building

   - [Local build instructions](https://infra.apache.org/asf-pelican-local.html)
   - [ASF YAML build](.asf.yaml) -- ASF infrastructure instructions

9. When you are ready to use this repository as the source for your live site, create a Jira ticket to ask Infra to adjust the build process. From then on, changes you make to the trunk of this repository automatically update the live site.

## Issues and template questions

Please let us know if you run into issues with the template.

   - [Issues](https://github.com/apache/template-site/issues)
