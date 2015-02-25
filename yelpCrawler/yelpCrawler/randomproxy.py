# Copyright (C) 2013 by Aivars Kalvans <aivars.kalvans@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import re
import random
import base64
from scrapy import log

class RandomProxy(object):
    def __init__(self, settings):
        self.proxy_list = settings.get('PROXY_LIST')
        self.proxies = {}
        for line in open(self.proxy_list, "r"):
            proxy = line.split()[0].strip()
            self.proxies[proxy] = proxy

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        item = random.choice(self.proxies.keys())
        proxy = self.proxies[item]
        request.meta['proxy'] = 'http://%s' % proxy
        print("request proxy" + request.url + "\t" + proxy)

    def process_exception(self, request, exception, spider):
        print(exception)
        if 'proxy' in request.meta:
            proxy = request.meta['proxy']
            log.msg('Removing failed proxy <%s>, %d proxies left' % (
                        proxy, len(self.proxies)))
            try:
                del self.proxies[proxy]
            except ValueError:
                pass