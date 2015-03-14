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

TIMEZONE = 'Europe/Zurich'

DEFAULT_LANG = u'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Disable tags
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

# Markdown extensions
MD_EXTENSIONS = ['def_list', 'sane_lists', 'tables']

# Pagination
DEFAULT_PAGINATION = 10

# Document-relative URLs when developing
RELATIVE_URLS = True

# Theme
THEME = 'themes/pelican-c4h'

# Static files
STATIC_PATHS = ['files']

# Primary navigation
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Home', '/'),
    ('Über uns', '/pages/about.html'),
    ('Reaktionen', '/pages/pressreview.html'),
    ('Presse', '/category/pressinfo.html'),
    ('Impressum', '/pages/imprint.html'),
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
