#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This is a collection of simple in-page callable tools for pelican.
To use a function, use the following syntax in your markdown:
` spu:command_name("arg1", "arg2", "arg3") `

In HTML, you would do:
<code> spu:command_name("arg1", "arg2") </code>

command_name must match a respective spu_cmd_* command in python.
"""
try:
    from pelican.plugins import signals
except ImportError:
    from pelican import signals
import pelican.contents
import requests
import urllib.parse
import fnmatch
import re

# List of subdomains deemed safe for spu:fetch()
SPU_FETCH_SAFE_DOMAINS = ("*.apache.org",)


def spu_cmd_fetch(args: list):
    """Fetches an external URL and put the content where the call was made"""
    url = args[0]
    url_parsed = urllib.parse.urlparse(url)
    is_safe = any(fnmatch.fnmatch(url_parsed.netloc, pattern) for pattern in SPU_FETCH_SAFE_DOMAINS)
    if is_safe:
        print("Fetching external resource " + url)
        return requests.get(url).text
    else:
        print("Not fetching unsafe external resource " + url)
        return ""


def spu_sub(call):
    my_functions = {k: v for k, v in globals().items() if callable(v) and k.startswith("spu_cmd_")}
    cmd = call.group(1)
    args = [x[1] for x in re.findall(r"(['\"]?)(.*?)\1(?:,\s*)?", call.group(2)) if x[1]]
    fnc = "spu_cmd_" + cmd
    if fnc in my_functions:
        return my_functions[fnc](args)
    return ""


def spu_parse(instance: pelican.contents.Page):
    if instance._content is not None:
        instance._content = re.sub(
            r"<code>\s*spu:([_a-z]+)\(((?:(['\"]?)(.*?)\3(?:,\s*)?)*)\s*?\)\s*<\/code>",
            spu_sub,
            instance._content,
            flags=re.UNICODE,
        )


def register():
    print("Simple Pelican Utils registered.")
    signals.content_object_init.connect(spu_parse)
