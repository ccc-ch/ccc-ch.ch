#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Chaos Computer Club Schweiz'
SITENAME = u'Chaos Computer Club Schweiz'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

MD_EXTENSIONS = ['def_list', 'smarty', 'sane_lists', 'tables']

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme
THEME = 'themes/ccczh'

# Show pages in primary nav
DISPLAY_PAGES_ON_MENU = True

# Use directories as categories
USE_FOLDER_AS_CATEGORY = True

# Date formats
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DATE_FORMATS = {
    'de': '%d.%m.%Y',
    'fr': '%d.%m.%Y',
    'it': '%d.%m.%Y',
    'en': '%Y-%m-%d',
}
