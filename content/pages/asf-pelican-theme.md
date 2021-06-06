Title: Apache Theme for ASF Pelican

The Apache Theme, created for use with [ASF-Pelican](asf-pelican.html) for project websites, is available at <a href="https://github.com/apache/www-site/tree/main/theme" target="_blank">github.com/apache/www-site/tree/main.theme</a>.

It has two types of files:

- Page templates
- CSS stylesheets

## Page templates

- base.html - the main template. Other templates extend this template automatically, including those in the default Pelican thme.
- page.html - this overrides Pelican's `default/simple page.html`, which includes `<h1>{{ page.title }}</h1>`. which we do not want.

Change `base.html` as necessary. Add new override templates if you need them.

See the <a href="https://docs.getpelican.com/en/latest/themes.html#inheritance" target="_blank">Pelican documentation</a> for information about inheritance from the simple theme.

## CSS stylesheets

In this site the css included by `base.html` is in the `content` tree.
There are site- or template-specific overrides to the stylesheet frameworks, but these are not done as Pelican specifies.

- `styles.css` - consists of custom site CSS overrides. Edit as needed. Here we include the CSS for the ASF permalink style.
  This file is in the same directory as the html and is included inline with `{% include "styles.css" %}`.

## Page metadata

This theme uses the following metadata:

- Title. Used in `base.html` with `<title>{{ page.title }}</title>` to provide the page title.

- Notice. This is notice text, which is typically a link to the license.

  `{% if page.notice %}<!-- {{ page.notice }} -->{% endif %}`

- License. This is an alternative to Notice.

- bodytag. This adds attributes to the `<body>` element.
  This is allows the main `index.ezmd` to have the same template, but with a different layout.

  `<body{% if page.bodytag %} {{ page.bodytag }}{% endif %} >`   

## Pelican settings

Manage Pelican settings in the `pelicanconf.py` file at the top level of the template.

Some important settings:

~~~python
SITEURL = 'https://www.apache.org'
SITEREPOSITORY = 'https://github.com/apache/www-site/blob/main/content/'
CURRENTYEAR = date.today().year
~~~

The file contains helpful comments about the settings.

- In `base.html`, use `CURRENTYEAR` for the copyright.

  `Copyright &#169; {{ CURRENTYEAR }} The Apache Software Foundation`


## Pelican theme

This is a [custom theme][1]. Pelican templates use [Jinja][2].

## History - Apache CMS

The [svn history](http://svn.apache.org/viewvc/infrastructure/site/trunk/templates) was not migrated and remains available.


[1]: https://docs.getpelican.com/en/latest/themes.html
[2]: https://jinja.palletsprojects.com/en/3.0.x/
