#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from Vantpy.Pages.BaiduPage import BaiduPage
from Vantpy.BaseSe.Selenium2 import Pyse
from Vantpy.Data.baidu_data import *
from Vantpy import logreport
log = logreport.Log()
class BaiduCase(unittest.TestCase):
    def setUp(self):
        self.driver = Pyse.browser()
        self.title = titleXlsx()
        self.url = UrlXlsx()

    def test_baidu1(self):
        baidu = BaiduPage(self.driver,self.url,self.title)
        baidu.open()
        baidu.input_baidu_text(StrXlsx())
        baidu.click_baidu_btn()

    def tearDown(self):
        driver = self.driver
        driver.quit()