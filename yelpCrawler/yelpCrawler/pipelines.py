# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class YelpcrawlerPipeline(object):
#     def process_item(self, item, spider):
#         return item

from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request
import json
import codecs

class restaurantPipeline(object):
    count = 0
    def __init__(self):
        self.file = codecs.open('restaurant.json', 'w', encoding='utf-8')
        
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)+"\n"
        print("dumping " + str(self.count))
        self.count += 1
        self.file.write(line)
        return item
    
    def spider_closed(self, spider):
        self.file.close()