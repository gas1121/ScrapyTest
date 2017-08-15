from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from scrapy.utils.reqser import request_to_dict, request_from_dict
from scrapy_splash import SplashRequest


class SplashRequestMiddleware(object):
    def process_request(self, request, spider):
        if "splash" in request.meta:
            return

        new_req = SplashRequest(url=request.url, callback=request.callback,
                                args={'wait': 0.5})
        req_dict = request_to_dict(new_req, spider)
        new_req = request_from_dict(req_dict, spider)
        new_req.dont_filter = True
        return new_req


class SeleniumDownloaderMiddleware(object):
    def process_request(self, request, spider):
        driver = webdriver.Remote(
            command_executor='http://phantomjs:8910',
            desired_capabilities=DesiredCapabilities.PHANTOMJS
        )
        driver.get(request.url)
        body = driver.page_source
        url = driver.current_url
        driver.close()
        return HtmlResponse(url, body=body,
                            request=request, encoding='utf-8')
