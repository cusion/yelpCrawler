from scrapy.contrib.spiders.crawl import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy import log

import re

from yelpCrawler.items import YelpcrawlerItem
from scrapy.log import level_names

class restaurantSpider(CrawlSpider):
    name = "restaurantSpider"
    allowed_domains = ["www.yelp.com",]
    start_urls = [
                  "http://www.yelp.com/search?find_desc=chinese+restaurant&find_loc=San+Francisco%2C+CA&ns=1&start=0&sortby=rating&l=g:-122.530517578,37.6859939294,-122.325897217,37.8488325065",
                 ]
#     start_urls = [line for line in open("yelpCrawler/seeds/restaurant.txt")]
    rules = [
            Rule(SgmlLinkExtractor(allow=(r"/search\?.*", ), restrict_xpaths=('//ul[@class="pagination-links"]')), follow=True, callback='parse_restaurant'),
#               Rule(SgmlLinkExtractor(allow=(r"/search\?.*start=\d+")),  follow=True, callback='parse_restaurant'),
            ]
    
    def parse_restaurant(self, response):
        items = []
#         print(response.url)
        sel = Selector(response)
        
        result_list = sel.css('div.content ul.ylist.ylist-bordered.search-results div.natural-search-result')
        
        # add this to retry another proxy
        if not result_list:
            log.msg("Retrying with " + response.url, level=log.INFO)
            yield Request(url=response.url, dont_filter=True)
        
        log.msg("Crawled "+response.url, level=log.INFO)
        for element in result_list:
            item = YelpcrawlerItem()
            item['name'] = clear_html_tag(trim_and_join(element.css('h3.search-result-title a.biz-name').xpath('text()').extract()))
#             print(type(element.css('h3.search-result-title a.biz-name').xpath('text()').extract()))
            item['rating'] = trim_and_join(element.css('div.rating-large i.star-img').xpath('@title').extract()).split()[0]
            item['review_count'] = trim_and_join(element.css('span.review-count').xpath('text()').extract()).split()[0]
#             print(type(element.css('span.review-count').xpath('text()').extract()))
            item['price_range'] = trim_and_join(element.css('div.price-category span.business-attribute.price-range').xpath('text()').extract()).count("$")
            item['location'] = trim_and_join(element.css('div.secondary-attributes address').xpath('text()').extract())
#             print(type(element.css('div.secondary-attributes address').xpath('text()').extract()))
            
#             items.append(item)
            yield item
        
#         yield items
    
class bankSpider(CrawlSpider):
    name = "bankSpider"
    allowed_domains = ["www.yelp.com",]
    
#     start_urls = ["http://www.yelp.com/search?find_loc=San+Francisco%2C+CA&ns=1&find_desc=bank&start=0&sortby=rating&l=g:-122.530517578,37.6859939294,-122.325897217,37.8488325065",]
    start_urls = [line for line in open("yelpCrawler/seeds/bank.txt")]
    
    rules = [
            Rule(SgmlLinkExtractor(allow=(r"/search\?.*", ), restrict_xpaths=('//ul[@class="pagination-links"]')), follow=True, callback='parse_bank'),
#               Rule(SgmlLinkExtractor(allow=(r"/search\?.*start=\d+")),  follow=True, callback='parse_restaurant'),
            ]
    def parse_bank(self, response):
        items = []
        sel = Selector(response)
        
        result_list = sel.css('div.content ul.ylist.ylist-bordered.search-results div.natural-search-result')
        
        # add this to retry another proxy
        if not result_list:
            yield Request(url=response.url, dont_filter=True)
        
        for element in result_list:
            item = YelpcrawlerItem()
            item['name'] = clear_html_tag(trim_and_join(element.css('h3.search-result-title a.biz-name').extract()))
#             print(type(element.css('h3.search-result-title a.biz-name').xpath('text()').extract()))
            item['rating'] = trim_and_join(element.css('div.rating-large i.star-img').xpath('@title').extract()).split()[0]
            item['review_count'] = trim_and_join(element.css('span.review-count').xpath('text()').extract()).split()[0]
#             print(type(element.css('span.review-count').xpath('text()').extract()))
            item['price_range'] = trim_and_join(element.css('div.price-category span.business-attribute.price-range').xpath('text()').extract()).count("$")
            item['location'] = trim_and_join(element.css('div.secondary-attributes address').xpath('text()').extract())
#             print(type(element.css('div.secondary-attributes address').xpath('text()').extract()))
            
#             items.append(item)
            yield item
        
#         yield items          # we cannot yield list, rather we should yield an item each time we want to append it into a list
    
class gasStationSpider(CrawlSpider):
    name = "gasStationSpider"
    allowed_domains = ["www.yelp.com",]
#     start_urls = ["http://www.yelp.com/search?find_loc=San+Francisco%2C+CA&ns=1&find_desc=gas+station&start=0&sortby=rating&l=g:-122.530517578,37.6859939294,-122.325897217,37.8488325065",]
    start_urls = [line for line in open("yelpCrawler/seeds/gas_station.txt")]
    
    rules = [
            Rule(SgmlLinkExtractor(allow=(r"/search\?.*", ), restrict_xpaths=('//ul[@class="pagination-links"]')), follow=True, callback='parse_gasStation'),
#               Rule(SgmlLinkExtractor(allow=(r"/search\?.*start=\d+")),  follow=True, callback='parse_restaurant'),
            ]
    def parse_gasStation(self, response):
        items = []
        sel = Selector(response)
        
        result_list = sel.css('div.content ul.ylist.ylist-bordered.search-results div.natural-search-result')
        
        # add this to retry another proxy
        if not result_list:
            yield Request(url=response.url, dont_filter=True)
        
        for element in result_list:
            item = YelpcrawlerItem()
            item['name'] = clear_html_tag(trim_and_join(element.css('h3.search-result-title a.biz-name').extract()))
#             print(type(element.css('h3.search-result-title a.biz-name').xpath('text()').extract()))
            item['rating'] = trim_and_join(element.css('div.rating-large i.star-img').xpath('@title').extract()).split()[0]
            item['review_count'] = trim_and_join(element.css('span.review-count').xpath('text()').extract()).split()[0]
#             print(type(element.css('span.review-count').xpath('text()').extract()))
            item['price_range'] = trim_and_join(element.css('div.price-category span.business-attribute.price-range').xpath('text()').extract()).count("$")
            item['location'] = trim_and_join(element.css('div.secondary-attributes address').xpath('text()').extract())
#             print(type(element.css('div.secondary-attributes address').xpath('text()').extract()))
            
#             items.append(item)
            yield item
        
#         yield items
    
class grocerySpider(CrawlSpider):
    name = "grocerySpider"
    allowed_domains = ["www.yelp.com",]
#     start_urls = ["http://www.yelp.com/search?find_loc=San+Francisco%2C+CA&ns=1&find_desc=asian+grocery+store&start=0&sortby=rating&l=g:-122.530517578,37.6859939294,-122.325897217,37.8488325065",]
    start_urls = [line for line in open("yelpCrawler/seeds/grocery_store.txt")]
    
    rules = [
            Rule(SgmlLinkExtractor(allow=(r"/search\?.*", ), restrict_xpaths=('//ul[@class="pagination-links"]')), follow=True, callback='parse_grocery'),
#               Rule(SgmlLinkExtractor(allow=(r"/search\?.*start=\d+")),  follow=True, callback='parse_restaurant'),
            ]
    def parse_grocery(self, response):
        items = []
        sel = Selector(response)
        
        result_list = sel.css('div.content ul.ylist.ylist-bordered.search-results div.natural-search-result')
        
        # add this to retry another proxy
        if not result_list:
            yield Request(url=response.url, dont_filter=True)
        
        for element in result_list:
            item = YelpcrawlerItem()
            item['name'] = clear_html_tag(trim_and_join(element.css('h3.search-result-title a.biz-name').extract()))
#             print(type(element.css('h3.search-result-title a.biz-name').xpath('text()').extract()))
            item['rating'] = trim_and_join(element.css('div.rating-large i.star-img').xpath('@title').extract()).split()[0]
            item['review_count'] = trim_and_join(element.css('span.review-count').xpath('text()').extract()).split()[0]
#             print(type(element.css('span.review-count').xpath('text()').extract()))
            item['price_range'] = trim_and_join(element.css('div.price-category span.business-attribute.price-range').xpath('text()').extract()).count("$")
            item['location'] = trim_and_join(element.css('div.secondary-attributes address').xpath('text()').extract())
#             print(type(element.css('div.secondary-attributes address').xpath('text()').extract()))
            
#             items.append(item)
            yield item
        
#         yield items
    
    
def clear_html_tag(content):
    content = re.sub('<[^>]*?>', '', content)
#     print(content)
    return content
    
def trim_and_join(field):
    if field is None or field==[]:
        field = ["NA",]
    ret = ""
    for ele in field:
        ret += ele.strip()+" "
    return ret[:-1]
    
    