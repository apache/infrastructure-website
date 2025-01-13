Title: ASF Pelican plugins
license: https://www.apache.org/licenses/LICENSE-2.0

**Note**
In 2019 Infra created ASF-Pelican as a structure and template for projects to use to build their websites, and for the ASF's own website.

In 2024, Infra moved from ASF-Pelican to the ASF **Infrastructure Pelican Action** GitHub Action to perform the same functions without being closely tied to BuildBot. The repository for this GHA is <a href="https//:github.com/apache/infrastructure-actions/tree/main/pelican" target="_blank">github.com/apache/infrastructure-actions/tree/main/pelican</a>.

The following material is correct for both ASF-Pelican and its replacement.

<hr/>

# Plugins
You can find the available plugins for a site using the ASF-Pelican template in the `themes/plugins` folder of your website's project repository.

# Plugin architecture

The plugins operate at various points in a Pelican build.

Pelican uses <a href="https://docs.getpelican.com/en/latest/plugins.html#list-of-signals" target="_blank">signals</a> at various points.

Here is a high-level review of the sequence of events:

## Pelican settings

Settings for a Pelican build are in your Pelican configuration file, `pelicanconf.py`. Here is where you list the plugins you are using.

```python
PLUGIN_PATHS = ['./theme/plugins']
PLUGINS = ['asfgenid', 'asfdata', 'pelican-gfm', 'asfreader']
```

## Initialization

At initialization, Pelican reads any ASF_DATA into a metadata dictionary that is available in every page in the site.

- The plugin `.asfdata.py` reads an `.asfdata.yaml` file and creates the metadata dictionary.

```python
ASF_DATA_YAML = ".asfdata.yaml"
ASF_DATA = {
    'data': ASF_DATA_YAML,
    'metadata': { },
    'debug': True
}
```

- The asfgenid plugin `./asfgenid.py` configures the site's features.

```python
# Configure the asfgenid plugin
ASF_GENID = {
    'metadata': True,
    'elements': True,
    'headings': True,
    'headings_re': r'^h[1-4]',
    'permalinks': True,
    'toc': True,
    'toc_headers': r"h[1-4]",
    'tables': True,
    'debug': False
}
```

## Readers (readers_init)

The system sets two important readers at this point. Readers are responsible for transforming page files to HTML and
providing a metadata dictionary.

- GFMReader by the pelican-gfm plugin. This code is in a private repository - ask Infra. Transforms GitHub Flavored Markdown(GFM) to HTML.
 
 * .md
  * .markdown
  * .mkd
  * .mdown

- `ASFReader, `.asfreader.py) transforms an <a href="https://github.com/gstein/ezt" target="_blank">ezt template</a> into GFM and then to HTML.
  
  * .ezmd

## Content init (content_object_init)

This is signaled after a reader has processed the site's content. At this point plugins can review, record, and transform the HTML content.

- The asfgenid plugin, `./asfgenid.py`, performs a number of steps. Some of the steps are optional.
  * Metadata transformation by looking up {{ key_expression }} in the page metadata.
  * Inventory of existing ID attributes.
  * Set ID and class attributes specified by {#id} and {.class} syntax.
  * Assign an ID to any headings without IDs.
  * Insert a table of contents if a [TOC] tag is present.

## Apache CMS

Many projects had their websites served by the Apache CMS from 2010. It was deprecated in 2021. The CMS was written in Perl. We have a new approach that fits Pelican. 

If you want to look into the old CMS process, its <a href="http://svn.apache.org/viewvc/infrastructure/site/trunk/lib/views" target="_blank">Subversion repository and history</a> remain available.
