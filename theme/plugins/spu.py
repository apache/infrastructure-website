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

command_name must match a respective su_cmd_* command in python.
"""
try:
    from pelican.plugins import signals
except ImportError:
    from pelican import signals
import pelican.contents
import requests
import re


def su_cmd_fetch(args):
    """Fetches an external URL and put the content where the call was made"""
    url = args[0]
    print("Fetching external resource " + url)
    return requests.get(url).text


def su_parse(instance: pelican.contents.Page):
    my_functions = {k:v for k, v in globals().items() if callable(v) and k.startswith('su_cmd_')}
    if instance._content is not None:
        content = instance._content
        for call in re.finditer(r"<code>\s*spu:([_a-z]+)\(((?:(['\"]?)(.*?)\3(?:,\s*)?)*)\s*?\)\s*<\/code>", content, flags=re.UNICODE):
            errything = call.group(0)
            cmd = call.group(1)
            args = [x[1] for x in re.findall(r"(['\"]?)(.*?)\1(?:,\s*)?", call.group(2)) if x[1]]
            fnc = "su_cmd_" + cmd
            if fnc in my_functions:
                retval = my_functions[fnc](args)
                content = content.replace(errything, retval, 1)
        if content != instance._content:
            instance._content = content


def register():
    print("Simple Pelican Utils registered.")
    signals.content_object_init.connect(su_parse)
