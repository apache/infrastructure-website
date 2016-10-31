Apache Infrastructure Website
=============================

## How to build Infra Site
This builds the website and puts pages in output/

    `virtualenv $venvname`
    `source $venvname/bin/activate`
    `pip install -r requirements.txt`
    Edit all the markdown! (pages/)
    `pelican content`

To preview:
    `python -m pelican.server`

