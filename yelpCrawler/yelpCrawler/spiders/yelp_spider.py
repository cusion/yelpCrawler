from scrapy.contrib.spiders.crawl import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from yelpCrawler.items import YelpcrawlerItem

class restaurantSpider(CrawlSpider):
    name = "restaurantSpider"
    allowed_domains = ["http://www.yelp.com",]
    start_urls = [
                  "http://www.yelp.com/search?find_desc=chinese+restaurant&find_loc=San+Francisco%2C+CA&ns=1#start=0&sortby=rating&l=g:-122.530517578,37.6859939294,-122.325897217,37.8488325065",
                 ]
    rules = [
            Rule(SgmlLinkExtractor(allow=(r"/search?[\s\S]*", ), restrict_xpaths=(r'//ul[@class="pagination-links"]')), follow=True, callback='parse_restaurant'),
            ]
    
    def parse_restaurant(self, response):
        items = []
        sel = Selector(response)
        
        result_list = sel.css('div.content ul.ylist.ylist-bordered.search-results')
        for element in result_list:
            item = YelpcrawlerItem()
            item['name'] = element.css('h3.search-result-title a.biz-name').xpath('text()').extract()
            item['rating'] = element.css('div.rating-large i.star-img').xpath('@title').extract().split()[0]
            item['review_count'] = element.css('div.rating-large span.review-count').xpath('text()').extract().split()[0]
            item['price_range'] = element.css('div.price-category span.business-attribute.price-range').xpath('text()').extract().count('$')
            item['location'] = element.css('div.secondary-attributes address').xpath('text()').extract()
            
            items.append(item)
        
        return items