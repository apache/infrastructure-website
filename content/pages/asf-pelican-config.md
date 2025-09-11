Title: Configuring ASF Pelican
license: https://www.apache.org/licenses/LICENSE-2.0

**Note**
In 2019 Infra created ASF-Pelican as a structure and template for projects to use to build their websites, and for the ASF's own website.

In 2024, Infra moved from ASF-Pelican to the ASF **Infrastructure Pelican Action** GitHub Action to perform the same functions without being closely tied to BuildBot. The repository for this GHA is <a href="https://github.com/apache/infrastructure-actions/tree/main/pelican" target="_blank">github.com/apache/infrastructure-actions/tree/main/pelican</a>.

This page was relevant to ASF-Pelican, but is **not relevant** to the replacement Pelican GitHub Action.

<hr/>

Review <a href="https://github.com/apache/template-site" target="_blank">github.com/apache/template-site</a> to inspect a full `pelicanconf.yaml` file.

These are the sections to configure in `pelicanconf.yaml` for your website: 

## Required

```
site:
  name: Apache Template
  description: Provides a template for projects wishing to use the Pelican ASF static content system
  domain: template.apache.org
  logo: images/logo.png
  repository: https://github.com/apache/template-site/blob/main/content/
  trademarks: Apache, the Apache logo, and "Project" are trademarks or registered trademarks

theme: theme/apache
```

## Options

### Plugins

If you are using the standard plugins included in ASF Pelican, you can leave this section out.
If you include it, your build will automatically include the `gfm` plugin.

```
plugins:
  paths:
    - theme/plugins
  use:
    - gfm
```

### Special setup

To configure four special features:

```
setup:
  data: asfdata.yaml
  run:
    - /bin/bash shell.sh
  ignore:
    - README.md
    - include
    - docs
  copy:
    - docs
```

1. data - uses `asfdata` plugin to build a data model to use in `ezmd` files. www-site is the best example.
2. run - uses `asfrun` plugin to run scripts. httpd-site's security vulnerability processing is the best example.
3. ignore - sets Pelican's IGNORE_FILES setting.
4. copy - uses `asfcopy` plugin to copy static files outside of the Pelican process. Include these in `ignore` as well.
   This is useful if you have large files or many static files.

## Generate ID

The `asfgenid` plugin performs a number of fixups and enhancements.

```
genid:
  unsafe: yes
  metadata: yes
  elements: yes
  headings_depth: 4
  permalinks: yes
  toc_depth: 4
  tables: yes
```
