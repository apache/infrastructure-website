Apache Infrastructure Website
=============================

This is the future of the Apache Infrastructure team's website.
Work in progress; this is the long-term replacement for infra.apache.org

## How to build the Infra Site:
This builds the website and puts its pages in output/

    `virtualenv $venvname`
    `source $venvname/bin/activate`
    `pip install -r requirements.txt`

    `git pull origin master`
    Edit all the markdown! (infrastructure-website/content/pages/)

    `pelican -t theme`

To preview:

    `cd output/`
    `python -m pelican.server`
    Browse to localhost:8000

## Technical site documentation:
Any time you check in a file, the site regenerates:
https://ci.apache.org/builders/infrastructure-website/

## Preparation
The `gfm_reader.py` script points to a specific directory on
bb-slave1 for loading the `libcmark-gfm.so` and `libcmark-gfmextensions.so`
libraries. The path should be adjusted for your local installation.

Run `build_cmark.sh` to build the two libraries. It is
then helpful to create a directory (say, `build_cmark/lib`) with
two symlinks from the `.so` to the longer, version-specific libraries
that the above shell script builds.
