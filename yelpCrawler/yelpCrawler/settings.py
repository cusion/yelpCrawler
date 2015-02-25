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
LOG_ENABLED = True
LOG_LEVEL = 'INFO'

# settings for using proxy; 
# from https://github.com/aivarsk/scrapy-proxies.git
RETRY_TIMES = 10  # times to retry every proxy
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]  # situations when we need to retry connection
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 300,
    # Fix path to this module
    'yelpCrawler.randomproxy.RandomProxy': 200,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 400,
}
PROXY_LIST = 'yelpCrawler/seeds/proxy_list.txt'   # format: (ip:port) without brackets 