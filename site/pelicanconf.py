#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Chaos Computer Club Schweiz'
SITENAME = u'Chaos Computer Club Schweiz'
SITEURL = ''

# Paths
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['news', 'protocols', 'pressinfo']

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

MD_EXTENSIONS = ['def_list', 'sane_lists', 'tables']

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme
THEME = 'themes/ccczh'

# Primary navigation
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Home', '/'),
    ('News', '/category/news.html'),
    ('Statuten', '/pages/statuten.html'),
    ('FAQ', '/pages/faq.html'),
    ('Presse', '/pages/pressespiegel.html'),
    ('Protokolle', '/category/protocols.html'),
    ('Pressemitteilungen', '/category/pressinfo'),
    ('Impressum', '/pages/impressum.html'),
)

# Metadata configuration
USE_FOLDER_AS_CATEGORY = False
SLUGIFY_SOURCE = 'basename'
PATH_METADATA = '(?P<slug>(?P<category>[a-zA-Z]+)/(?P<date>\d{4}-\d{2}-\d{2})_[^/]+)/(?P<lang>[a-z].*).md'

# Date formats
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DATE_FORMATS = {
    'de': '%d.%m.%Y',
    'fr': '%d.%m.%Y',
    'it': '%d.%m.%Y',
    'en': '%Y-%m-%d',
}

# Typography
TYPOGRIFY = True
