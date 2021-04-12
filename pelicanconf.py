#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Predrag TASEVSKI - Pece'
SITENAME = u'Predrag TASEVSKI - Pece'
SITEURL = 'https://predragtasevski.com'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category/{slug}.atom.xml'
TAG_FEED_ATOM = 'feeds/tag/{slug}.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/category/%s.atom.xml'

# Blogroll
LINKS = (('Cybersecurity.mk', 'http://cybersecurity.mk/'),
         ('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Linkedin', 'https://www.linkedin.com/in/tpredrag'),
        ('Twitter', 'https://twitter.com/stepcellwolf'),
        ('Github', 'https://github.com/stepcellwolf/'),
        ('Google+', 'https://plus.google.com/u/0/+PredragTasevski/posts/p/pub'),
        ('Flickr', 'https://www.flickr.com/photos/29569957@N00'),
        ('RSS', '/feeds/all.atom.xml'),
	    ('Instagram', 'https://www.instagram.com/stepcellwolf/'),
        ('🏃🏻‍♂️ Strava', 'https://www.strava.com/athletes/60401767'),)

# Feeds
FEEDS =  (('All posts', 'feeds/all.atom.xml'),
                  ('Category', 'feeds/category'),)

DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Formatting for dates

DEFAULT_DATE_FORMAT = ('%a, %d %b %Y')

# category to fall back on
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'pages'
#INDEX_SAVE_AS = 'blog_index.html'

#PAGINATION_PATTERNS = (
#    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
#)

# Formatting for urls

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"
DISPLAY_TAGS_ON_SIDEBAR = True
TAG_CLOUD_MAX_ITEMS = 70

PAGE_URL = 'pages/{slug}.html'


# Generate yearly archive

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Show most recent posts first

NEWEST_FIRST_ARCHIVES = True

# Specify theme

THEME = "/Users/pece/dev/pelican-themes/pelican-bootstrap3"

# Plugins

PLUGIN_PATHS = ["plugins","/Users/pece/dev/pelican-plugins"]
PLUGINS = ['neighbors', 'summary', 'tag_cloud', 'related_posts','i18n_subsites',]

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Gallery

#PHOTO_LIBRARY = "images/gallery/kozjak"
#PHOTO_GALLERY = (1024, 768, 80)
#PHOTO_THUMB = (192, 144, 60)



RELATED_POSTS_MAX = 10
PYGMENTS_STYLE = "emacs"
CC_LICENSE = "CC-BY-ND"
#DIRECT_TEMPLATES = (('search',))
TWITTER_USERNAME = "stepcellwolf"
TWITTER_WIDGET_ID = "645620628771504129"
#DISQUS_SITENAME = "predragtasevskipece"

# Only use LaTeX for selected articles

LATEX = 'article'

STATIC_PATHS = ['pages', 'extra/CNAME', 'extra/README', ]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},'extra/README':{'path': 'README'},}


#FLICKR
#FLICKR_API_KEY = '4578fbd42e4b8cf94b01fd02f3691105'
#FLICKR_USER = '29569957@N00'
#FLICKR_SETS_EXCLUDE = ['Compromising pictures', ]
#FLICKR_OUTPUT_DIRNAME = 'img'
#FLICKR_UPDATE = False

# Following items are often useful when publishing

#DISQUS_SITENAME = 'predragtasevskipece'
GOOGLE_ANALYTICS = 'UA-600234-3'
