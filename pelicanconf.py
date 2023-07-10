#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from datetime import datetime
import pytz

AUTHOR = 'Yeroda'
SITENAME = 'YERODA'
# SITEURL = ''
SITEURL = 'https://yeroda.com'

SITETITLE = "Reviews of Best Selling Products in 2023"
SITEDESCRIPTION = "Discover 2023's best-selling products with our reviews. Make informed purchases with our recommendations. Your shortcut to the best of 2023 starts here!"
SITEKEYWORDS = "Best Selling Products 2023"


TIMEZONE = 'Europe/Paris'
BUILD_TIME = datetime.now(pytz.timezone(TIMEZONE))

PATH = 'content'

THEME = 'theme/mulberry'


DEFAULT_LANG = 'en'

GOOGLE_ANALYTICS = "G-S5LW93DGNV"

LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# DEFAULT_ORPHANS = 0
DEFAULT_PAGINATION = 8 #6

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'


STATIC_PATHS = ['extra/robots.txt']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'}
}


SITEMAP = {
	"format": "xml",
    "exclude": ["tag/", "category/", "terms-and-conditions/", "disclaimer/", "privacy-policy/", "author/"]
}

PLUGIN_PATHS = ["plugins"]
# PLUGINS = ['sitemap','rad', 'yaml_metadata','more_categories', 'similar_posts']#, 'seo']
PLUGINS = ['sitemap','rad','more_categories', 'similar_posts']#, 'seo']

SIMILAR_POSTS_MAX_COUNT = 4

SEO_REPORT = False
SEO_ENHANCER = False
SEO_ENHANCER_OPEN_GRAPH = False
SEO_ENHANCER_TWITTER_CARDS = False

DELETE_OUTPUT_DIRECTORY = True
