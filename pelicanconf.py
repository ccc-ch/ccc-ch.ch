# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'CCC-CH'
SITENAME = u'CCC-CH'
SITEURL = u'https://www.ccc-ch.ch'
TIMEZONE = u'Europe/Zurich'
DEFAULT_LANG = u'de'
DEFAULT_DATE_FORMAT = '%a %d. %B %Y'

# Page path
PAGE_PATHS = ['pages']

# Menu
MENUITEMS = (
              ('Home', 'index.html', None),
              ('CCC-CH', '#', [
                ('FAQ', 'faq.html'),
                ('Statuten', 'statuten.html'),
                ('Mitglieder', 'members.html'),
              ]),
              ('Medienmitteilungen', 'category_medien.html', None),
              ('Pressereaktionen', 'category_pressreview.html', None),
              ('Intern', '#', [
                ('Protokolle', 'protokolle.html'),
                ('Mitgliederbeiträge', 'mitgliederbeitraege.html'),
                ('Gettogether', 'gettogether.html'),
                ('Schleuder', 'schleuder.html'),
              ]),
            )

# Sole author and don't use categories ... disable these features
#AUTHOR_SAVE_AS = ''
#AUTHORS_SAVE_AS = ''
#CATEGORY_SAVE_AS = ''
#CATEGORIES_SAVE_AS = ''

# don't show categories and pages in the menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_RSS = None
FEED_ALL_ATOM = None
FEED_RSS = 'feeds/rss.xml'
FEED_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = 'feeds/atom_%s.xml'
CATEGORY_FEED_RSS = 'feeds/rss_%s.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL settings
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
ARTICLE_URL = '{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tag-{slug}.html'
TAG_SAVE_AS = 'tag-{slug}.html'
TAGS_URL = 'tags.html'
TAGS_SAVE_AS = 'tags.html'
ARCHIVES_URL = 'archives.html'
ARCHIVES_SAVE_AS = 'archives.html'
CATEGORY_URL = 'category_{slug}.html'
CATEGORY_SAVE_AS = 'category_{slug}.html'

# Contact
EMAIL_ADDR = 'webmaster@ccc-ch.ch'

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']

# Plugin configuration
I18N_SUBSITES = {
  'de': {
    'LOCALE': 'de_CH'
  },
  'en': {
    'LOCALE': 'en_US'
  }
}

# Theme
THEME = 'theme'
STATIC_PATHS = ['images', 'media', 'articles', 'docs', 'extra/robots.txt', 'extra/favicon.ico', 'extra/htaccess']
PATH_METADATA = 'pages/(?P<path>.*)\..*'
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/htaccess': {'path': '.htaccess'},
}

# Licence
LICENCE_NAME = 'BY-NC-SA'
LICENCE_URL = 'http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US'
LICENCE_URL_IMG = 'http://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png'

# Tag cloud
TAG_CLOUD_STEPS = 4
