import unittest
from Pages.BaiduPage import BaiduPage
from Base.Selenium2 import BasePage

class BaiduCase(unittest.TestCase):
    def setUp(self):
        self.driver = BasePage.browser()
        self.title = '百度一下，你就知道'
        self.url = 'https://www.baidu.com'

    def test_baidu1(self):
        baidu = BaiduPage(self.driver,self.url,self.title)
        baidu.open()
        baidu.input_text('selenium')
        baidu.click_baidu_btn()

    def tearDown(self):
        driver = self.driver
        driver.quit()