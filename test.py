from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor='http://phantomjs:8910',
    desired_capabilities=DesiredCapabilities.PHANTOMJS)

driver.get('https://hlo.tohotheater.jp/net/schedule/076/TNPI2000J01.do')
print(driver.title)
print(driver.page_source)

driver.quit()
