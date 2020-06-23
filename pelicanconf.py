#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

import sys
import os


AUTHOR = u'PonyGnomeBot'
SITENAME = u'Apache Infrastructure'
SITEURL = ''
CURRENTYEAR = date.today().year

PATH = 'content'

TIMEZONE = 'UTC'
DEFAULT_DATE = 'fs'
DEFAULT_LANG = u'en'
SITEURL = 'https://infra-test.apache.org'

# Save pages using full directory preservation
PATH_METADATA= '.*?(pages/)?(?P<path_no_ext>.*?)\.[a-z]*$'
PAGE_SAVE_AS= './{slug}.html'
PAGE_URL= './{slug}.html'

# Make .htaccess static. Set up to add favicon in 'extra' folder
STATIC_PATHS = [
   'pages/.htaccess'
   'extra'
]

# Favicon for site
EXTRA_PATH_METADATA = {
   'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Standard behavior:
#PAGE_SAVE_AS = './{slug}.html'

#ARTICLE_SAVE_AS = 'news/{slug}.html'
#ARTICLE_URL = 'news/{slug}.html'

# Sort news by date, descending, latest article first
ARTICLE_ORDER_BY = 'reversed-date'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# TOC Generator
PLUGIN_PATHS = ['./theme/plugins']
PLUGINS = ['toc', 'pelican-gfm']
TOC_HEADERS = r"h[1-6]"

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
