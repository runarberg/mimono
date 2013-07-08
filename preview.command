#!/bin/sh
cd "`dirname "$0"`"

pelican -s devconf.py

cd webpage-dev
python -m "SimpleHTTPServer"
