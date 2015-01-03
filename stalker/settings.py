# -*- coding: utf-8 -*-

# Scrapy settings for stalker project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import sys
import os

BOT_NAME = 'stalker'

SPIDER_MODULES = ['stalker.spiders']
NEWSPIDER_MODULE = 'stalker.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'stalker (+http://www.yourdomain.com)'

# integration with django
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DJANGO_SITE_DIR = os.path.normpath(os.path.join(BASE_DIR, '../xgunicorn'))
sys.path.append(DJANGO_SITE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'xgunicorn.settings'

ITEM_PIPELINES = {
    'stalker.pipelines.StalkerPipeline': 1000
}