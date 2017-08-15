import scrapy
from scrapy_splash import SplashRequest


class SplashSpider(scrapy.Spider):
    name = "splash"
    start_urls = ['https://hlo.tohotheater.jp/net/schedule/076/TNPI2000J01.do']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        with open('test.html', 'wb') as f:
            f.write(response.body)
        return
