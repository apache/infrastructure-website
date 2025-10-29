Apache Infrastructure Website
=============================


This is the source of the Apache Infrastructure team's website, 
found at https://infra.apache.org/ 

## How to build the Infra Site:
This builds the website and puts its pages in site-generated/

```bash
# Fetch the repository containing the plugins:
git clone [-depth 1] https://github.com/apache/infrastructure-actions

# Fetch this repository
git clone [-depth 1] https://github.com/apache/infrastructure-website
cd infrastructure-website

virtualenv $venvname
source $venvname/bin/activate
pip install -r requirements.txt

git pull origin master

# Edit all the markdown! (infrastructure-website/content/pages/)

# Run Pelican build:
pelican content -e PLUGIN_PATHS='["../infrastructure-actions/pelican/plugins"]' -o site-generated $FLAGS

# $FLAGS are optional flags:
# -l start a webserver at http://127.0.0.1:8000/
# -r autoreload if any files change
```

## Technical site documentation
Any time you check in a file, the site regenerates:
https://ci2.apache.org/#/builders/3

## Preparation
The `gfm_reader.py` script points to a specific directory on
bb-slave1 for loading the `libcmark-gfm.so` and `libcmark-gfmextensions.so`
libraries. The path should be adjusted for your local installation.

Run `build_cmark.sh` to build the two libraries. It is
then helpful to create a directory (say, `build_cmark/lib`) with
two symlinks from the `.so` to the longer, version-specific libraries
that the above shell script builds.

## Preview PRs
To stage a preview of what a PR would result in, be sure to name your branches 
using the `preview/$foo` syntax, for instance `preview/cleanup-dec-2021`. This 
will auto-build and -stage your changes and make them available at 
`infrastructure-$foo.staged.apache.org`, e.g. `infrastructure-cleanup-dec-2021.staged.apache.org`

Note that underscore is not allowed in DNS,
so should not be used in the branch name.
