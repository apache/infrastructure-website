Apache Infrastructure Website
=============================

This is the future of the Apache Infrastructure team's website.
Work in progress; this is the long-term replacement for infra.a.o

## How to build Infra Site:
This builds the website and puts pages in output/

    `virtualenv $venvname`
    `source $venvname/bin/activate`
    `pip install -r requirements.txt`

    `git checkout https://github.com/apache/infrastructure-website`
    Edit all the markdown! (infrastructure-website/content/pages/)

    `cd infrastrucure-website`
    `pelican content -t theme`

To preview:

    `cd infrastructure-website/output/`
    `python -m pelican.server`
    Browse to localhost:8000

## Technical site documentation:
Anytime you checkin a file, the site is regenerated:
https://ci.apache.org/builders/infra-site
