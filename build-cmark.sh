#!/bin/bash
#
# Build the cmark-gfm library and extensions within CURRENT DIRECTORY.
#
# USAGE:
#   $ build-cmark.sh [ VERSION [ TARDIR ] ]
#
#   VERSION: defaults to 0.28.3.gfm.12
#   TARDIR: where to find a downloaded/cached tarball of the cmark
#           code, or where to place a tarball
#

# Echo all of our steps
set -x

#VERSION=0.28.3.gfm.20  ### not yet
VERSION=0.28.3.gfm.12
if [ "$1" != "" ]; then VERSION="$1"; fi

# The tarball exists here, or will be downloaded here.
TARDIR="."
if [ "$2" != "" ]; then TARDIR="$2"; fi

ARCHIVES="https://github.com/github/cmark-gfm/archive/refs/tags"
LOCAL="${TARDIR}/cmark-gfm.$VERSION.orig.tar.gz"

# WARNING: this must agree with the parent directory in the tar file or the build will fail
EXTRACTED_AS="cmark-gfm-$VERSION"

# Follow redirects, and place the result into known name $LOCAL
if [ -f "$LOCAL" ]; then
    echo "Using cached tarball: ${LOCAL}"
else
    echo "Fetching from cmark archives"
    curl -L -o "$LOCAL" "$ARCHIVES/$VERSION.tar.gz" || exit 1
fi

# Clean anything old, then extract and build.
### somebody smart could peek into the .tgz. ... MEH
if [ -d "$EXTRACTED_AS" ]; then rm -r "$EXTRACTED_AS"; fi
tar xzf "$LOCAL"
pushd "$EXTRACTED_AS"
  mkdir build
  pushd build
    cmake -DCMARK_TESTS=OFF -DCMARK_STATIC=OFF ..
    make
  popd

  mkdir lib
  cp -Pp build/src/lib* lib/
  cp -Pp build/extensions/lib* lib/
popd

# These files/dir may need a reference with LD_LIBRARY_PATH.
# gfm.py wants this lib/ in LIBCMARKDIR.
ls -laF "$EXTRACTED_AS/lib/"

# Provide a handy line for copy/paste.
echo "export LIBCMARKDIR='$(pwd)/$EXTRACTED_AS/lib'"
