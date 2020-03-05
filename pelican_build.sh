#!/bin/bash
# Test script for custombuilder
pip3 install -r requirements.txt
pelican -t theme content -o output
