#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys

AUTHOR = u'Chantal Uto'
SITENAME = u'MIMONO'
SITEURL = 'http://127.0.0.1:8000'

PATH = 'articles'
OUTPUT_PATH = 'webpage-dev'

DEFAULT_LANG = u'en'
TIMEZONE = 'Atlantic/Reykjavik'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'is': '%d. %B %Y',
}

THEME = "theme"
IGNORE_FILES = ['.#*', '*~', 'TODO']

sys.path.append('plugins')
PLUGINS = ['figurize',]

RELATIVE_URLS = False

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
