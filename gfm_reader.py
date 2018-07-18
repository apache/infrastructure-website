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
#
# gfm_reader.py -- GitHub-Flavored Markdown reader for Pelican
#

import sys
import os
import ctypes

import pelican.readers

_LIBDIR = '/home/buildslave/slave/tools/lib'
if sys.platform == 'darwin':
  _LIBCMARK = 'libcmark-gfm.dylib'
elif sys.platform == 'windows':
  _LIBCMARK = 'cmark-gfm.dll'
else:
  _LIBCMARK = 'libcmark-gfm.so'
try:
  cmark = ctypes.CDLL(os.path.join(_LIBDIR, _LIBCMARK))
except OSError:
  raise ImportError('%s not found. see build-mark.sh and gfm_reader.py'
                    % _LIBCMARK)

# Options for the GFM rendering call
OPTS = 0


class GFMReader(pelican.readers.BaseReader):

  enabled = True  # if we got here, the library is available

  if cmark:
    render = cmark.cmark_markdown_to_html
    render.restype = ctypes.c_char_p
    render.argtypes = (ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int)

  def read(self, source_path):
    "Parse content and metadata of GFM source files."

    # Fetch the source content, with some like 
    text = pelican_open(source_path)

    if sys.version_info >= (3, 0):
      text = text.encode('utf-8')
      content = GFMReader.render(text, len(text), OPTS).decode('utf-8')
    else:
      content = GFMRender.render(text, len(text), OPTS)

    metadata = { }
    ### extract metadata

    return content, metadata
