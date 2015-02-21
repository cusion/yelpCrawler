# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy import Item, Field


class YelpcrawlerItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    rating = Field()
    review_count = Field()
    price_range = Field()
    location = Field()
