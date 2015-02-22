# -*- coding: utf-8 -*-
from scrapy.settings.default_settings import LOG_LEVEL

# Scrapy settings for yelpCrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'yelpCrawler'

SPIDER_MODULES = ['yelpCrawler.spiders']
NEWSPIDER_MODULE = 'yelpCrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'yelpCrawler (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
                  'yelpCrawler.pipelines.jsonDumpPipeline' : 100,
                  }
LOG_ENABLED = False
# LOG_LEVEL = 'DEBUG'