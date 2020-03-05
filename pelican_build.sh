#!/bin/bash
pip3 install -r requirements.txt
pelican -t theme content -o output
