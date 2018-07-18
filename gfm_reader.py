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
import time

import pelican.readers
import pelican.utils

_LIBDIR = '/home/buildslave/slave/tools/lib'
if sys.platform == 'darwin':
  _LIBCMARK = 'libcmark-gfm.dylib'
  _LIBEXT = 'libcmark-gfmextensions.dylib'
elif sys.platform == 'windows':
  _LIBCMARK = 'cmark-gfm.dll'
  _LIBEXT = 'cmark-gfmextensions.dll'
else:
  _LIBCMARK = 'libcmark-gfm.so'
  _LIBEXT = 'libcmark-gfmextensions.so'
try:
  cmark = ctypes.CDLL(os.path.join(_LIBDIR, _LIBCMARK))
  cmark_ext = ctypes.CDLL(os.path.join(_LIBDIR, _LIBEXT))
except OSError:
  raise ImportError('%s not found. see build-mark.sh and gfm_reader.py'
                    % _LIBCMARK)

# Options for the GFM rendering call
### this could be moved into SETTINGS or somesuch, but meh. not needed now.
OPTS = 0

# The GFM extensions that we want to use
EXTENSIONS = (
  'autolink',
  'table',
  'strikethrough',
  'tagfilter',
  )


class GFMReader(pelican.readers.BaseReader):
  """GFM-flavored Reader for the Pelican system.

  Pelican looks for all subclasses of BaseReader, and automatically
  registers them for the file extensions listed below. Thus, nothing
  further is required by users of this Reader.
  """

  # NOTE: the builtin MarkdownReader must be disabled. Otherwise, it will be
  #       non-deterministic which Reader will be used for these files.
  file_extensions = ['md', 'markdown', 'mkd', 'mdown']

  def read(self, source_path):
    "Parse content and metadata of GFM source files."

    # Fetch the source content, with a few appropriate tweaks
    with pelican.utils.pelican_open(source_path) as text:
      if sys.version_info >= (3, 0):
        text = text.encode('utf-8')
        content = render(text).decode('utf-8')
      else:
        content = render(text)

    ### make up a title
    slug = '/'.join(source_path.split('/')[-2:])
    metadata = {
      'slug': slug,
      'title': 'gstein was here',  ### clearly wrong
#      'date': pelican.utils.set_date_tzinfo(time.gmtime()),  ### way wrong
      }
    ### extract metadata

    return content, metadata


def render(text):
  parser = F_cmark_parser_new(OPTS)
  assert parser
  for name in EXTENSIONS:
    ext = F_cmark_find_syntax_extension(name)
    assert ext
    rv = F_cmark_parser_attach_syntax_extension(parser, ext)
    assert rv
  exts = F_cmark_parser_get_syntax_extensions(parser)

  F_cmark_parser_feed(parser, text, len(text))
  doc = F_cmark_parser_finish(parser)
  assert doc

  output = F_cmark_render_html(doc, OPTS, exts)

  F_cmark_parser_free(parser)
  F_cmark_node_free(doc)

  return output


F_cmark_parser_new = cmark.cmark_parser_new
F_cmark_parser_new.res_type = ctypes.c_void_p
F_cmark_parser_new.arg_types = (ctypes.c_int,)

F_cmark_parser_feed = cmark.cmark_parser_feed
F_cmark_parser_feed.res_type = None
F_cmark_parser_feed.arg_types = (ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t)

F_cmark_parser_finish = cmark.cmark_parser_finish
F_cmark_parser_finish.res_type = ctypes.c_void_p
F_cmark_parser_finish.arg_types = (ctypes.c_void_p,)

F_cmark_parser_attach_syntax_extension = cmark.cmark_parser_attach_syntax_extension
F_cmark_parser_attach_syntax_extension.res_type = ctypes.c_int
F_cmark_parser_attach_syntax_extension.arg_types = (ctypes.c_void_p, ctypes.c_void_p)

F_cmark_parser_get_syntax_extensions = cmark.cmark_parser_get_syntax_extensions
F_cmark_parser_get_syntax_extensions.res_type = ctypes.c_void_p
F_cmark_parser_get_syntax_extensions.arg_types = (ctypes.c_void_p,)

F_cmark_parser_free = cmark.cmark_parser_free
F_cmark_parser_free.res_type = None
F_cmark_parser_free.arg_types = (ctypes.c_void_p,)

F_cmark_node_free = cmark.cmark_node_free
F_cmark_node_free.res_type = None
F_cmark_node_free.arg_types = (ctypes.c_void_p,)

F_cmark_find_syntax_extension = cmark.cmark_find_syntax_extension
F_cmark_find_syntax_extension.res_type = ctypes.c_void_p
F_cmark_find_syntax_extension.arg_types = (ctypes.c_char_p,)

F_cmark_render_html = cmark.cmark_render_html
F_cmark_render_html.res_type = ctypes.c_char_p
F_cmark_render_html.arg_types = (ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)


# Set up the libcmark-gfm library and its extensions
F_register = cmark_ext.core_extensions_ensure_registered
F_register.res_type = None
F_register.arg_types = ( )
F_register()

### technically, maybe install an atexit() to release the plugins
