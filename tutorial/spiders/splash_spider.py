import time
import scrapy
from scrapy_splash import SplashRequest


class SplashSpider(scrapy.Spider):
    name = "splash"
    #start_urls = ['https://hlo.tohotheater.jp/net/schedule/076/TNPI2000J01.do']
    start_urls = ['https://www.baidu.com']

    def start_requests(self):
        self.start = time.time()
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})
            #yield scrapy.Request(url, self.parse)

    def parse(self, response):
        self.end = time.time()
        print(self.end - self.start)        
        with open('test.html', 'w') as f:
            #f.write(response.body)
            f.write(response.text)
        return
