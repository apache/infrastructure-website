#!/bin/sh
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# build-cmark.sh -- build the GFM cmark library into a .so
#
#
# BUILD PREREQUISITES
#
#   * CMake
#
#

ARCHIVES="https://github.com/github/cmark/archive"
VERSION=0.28.3.gfm.12
LOCAL="cmark-gfm.$VERSION.orig.tar.gz"

# Echo all of our steps
set -x

# Put everything down in here, to keep things clean
mkdir -p build-cmark && cd build-cmark

# Follow redirects, and place the result into known name $LOCAL
curl -L -o "$LOCAL" "$ARCHIVES/$VERSION.tar.gz"

# Expand...
rm -r "cmark-$VERSION"
tar xzf "$LOCAL"
cd "cmark-$VERSION"
mkdir build && cd build
cmake -DCMARK_TESTS=OFF -DCMARK_STATIC=OFF ..
make

echo "NOTE: see build-cmark/cmark-$VERSION/build/src/libcmark-gfm.so"
echo "NOTE: see build-cmark/cmark-$VERSION/build/extensions/libcmark-gfmextensions.so"
