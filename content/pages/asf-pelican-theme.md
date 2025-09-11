Title: Apache Theme for ASF Pelican
license: https://www.apache.org/licenses/LICENSE-2.0

**Note**
In 2019 Infra created ASF-Pelican as a structure and template for projects to use to build their websites, and for the ASF's own website.

In 2024, Infra moved from ASF-Pelican to the ASF **Infrastructure Pelican Action** GitHub Action to perform the same functions without being closely tied to BuildBot. The repository for this GHA is <a href="https://github.com/apache/infrastructure-actions/tree/main/pelican" target="_blank">github.com/apache/infrastructure-actions/tree/main/pelican</a>.

The following material is correct for both ASF-Pelican and its replacement.
<hr/>
The Apache Theme is available at <a href="https://github.com/apache/template-site/tree/main/theme" target="_blank">github.com/apache/template-site/tree/main.theme</a>, in the "gha-compliant" branch.

It has two types of files:

- Page templates
- CSS stylesheets

## Page templates

- base.html - the main template. Other templates extend this template automatically, including those in the default Pelican theme.
- page.html - this overrides Pelican's `default/simple page.html`, which includes `<h1>{{ page.title }}</h1>`, which we do not want.

Change `base.html` as necessary. Add new override templates if you need them.

See the <a href="https://docs.getpelican.com/en/latest/themes.html#inheritance" target="_blank">Pelican documentation</a> for information about inheritance from the simple theme.

## CSS stylesheets

In this site the css included by `base.html` is in the `content` tree.
There are site- or template-specific overrides to the stylesheet frameworks, but these are not done as Pelican specifies.

- `styles.css` - consists of custom site CSS overrides. Edit as needed. Here we include the CSS for the ASF permalink style.
  This file is in the same directory as the HTML and is included inline with `{% include "styles.css" %}`.

## Page metadata

This theme uses the following metadata:

- Title. Used in `base.html` with `<title>{{ page.title }}</title>` to provide the page title.

- Notice. This is notice text, which is typically a link to the license.

  `{% if page.notice %}<!-- {{ page.notice }} -->{% endif %}`

- License. This is an alternative to Notice.

- bodytag. This adds attributes to the `<body>` element.
  This allows the main `index.ezmd` to have the same template, but with a different layout.

  `<body{% if page.bodytag %} {{ page.bodytag }}{% endif %} >`   

## Pelican settings

Manage Pelican settings in the <a href="https://github.com/apache/template-site/blob/main/pelicanconf.yaml" target="_blank">pelicanconf.yaml</a> file at the top level of the template.

Some important settings:

```

site:
  name: NAME OF YOUR SITE
  description: DESCRIPTION OF YOUR SITE
  domain: YOURSITE.apache.org
  logo: images/logo.png
  repository: https://github.com/apache/YOUR_REPO/blob/main/content/
  trademarks: Apache, the Apache logo, and "Project" are trademarks or registered trademarks
  
```


## Pelican theme

This is a [custom theme][1] Pelican templates use [Jinja][2].


<hr />

### Pelican variables set in pelicanconf.py

**Note**: early users of this template worked with `pelicanconf.py`, which is not part of the latest release. This information is for their convenience.

~~~python
SITENAME = u'Apache <pmc>'
SITEDOMAIN = '<pmc>.apache.org'
SITEURL = 'https://<pmc>.apache.org'
SITELOGO = 'https://<pmc>.apache.org/images/logo.png'
SITEDESC = u'<pmc desc>'
SITEREPOSITORY = 'https://github.com/apache/<pmc-site>/blob/<branch>/content/'
TRADEMARKS = u'Apache, the Apache logo, and <pmc> are trademarks or registered trademarks'
CURRENTYEAR = date.today().year
~~~


[1]: https://docs.getpelican.com/en/latest/themes.html
[2]: https://jinja.palletsprojects.com/en/3.0.x/
