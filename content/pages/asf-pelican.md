Title: ASF-Pelican
license: https://www.apache.org/licenses/LICENSE-2.0

In 2019 Infra created ASF-Pelican as a structure and template for projects to use to build their websites, and for the ASF's own website.

In 2024, Infra moved from ASF-Pelican to the ASF **Infrastructure Pelican Action** GitHub Action to perform the same functions without being closely tied to BuildBot. The repository for this GHA is <a href="https://github.com/apache/infrastructure-actions/tree/main/pelican" target="_blank">github.com/apache/infrastructure-actions/tree/main/pelican</a>.

Review the following information to simplify your work with, and get your best results from, the Pelican GHA:

## Getting started

See the [Pelican getting-started guide](asf-pelican-gettingstarted.html).

## For site designers

-  Information about the [ASF Theme](asf-pelican-theme.html).
-  The <a href="https://whimsy.apache.org/site/" target="_blank">Apache Project Website Checker</a> periodically reviews all TLP websites and reports whether they comply with Apache's <a href="https://www.apache.org/foundation/marks/pmcs#navigation" target="_blank">policies for TLP websites</a>.

## For site developers

-  [Data modeling](asf-pelican-data.html) provides what developers need to know to maintain and expand on the data they want to use and display on their site.
-  [Build process](asf-pelican-build.html) describes the full end-to-end build from the developer's perspective.
-  Review the [plugins](asf-pelican-plugins.html) that are included in the template repository, and the plugin architecture.

## For site committers

- The template uses [GitHub Flavored Markdown](gfm.html) (GFM) to structure content. It also supports most HTML elements.
- How to develop your site using [local builds](asf-pelican-local.html) on a local Linux or macOS system.
