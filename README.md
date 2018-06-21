Apache Infrastructure Website
=============================

This is the future of the Apache Infrastructure team's website.
Work in progress; this is the long-term replacement for infra.a.o

## How to build Infra Site:
This builds the website and puts pages in output/

    `virtualenv $venvname`
    `source $venvname/bin/activate`
    `pip install -r requirements.txt`
    Edit all the markdown! (pages/)
    `pelican content`

To preview:

    `python -m pelican.server`

## Technical site documentation:
Anytime you checkin a file, the site is regenerated:
https://ci.apache.org/builders/infra-site
