#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Email   : 944921374@qq.com

from selenium.webdriver.common.by import By
from test.common.Seleniums import BasePage
import sys
sys.path.append('../')
class BaiduPage(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    search_loc = (By.XPATH,'//*[@id="kw"]')#定位百度文本框
    click_btn = (By.XPATH,'//*[@id="su"]')#定位百度按钮

    def input_baidu_text(self,text):
        self.send_key(self.search_loc,text)

    def click_baidu_btn(self):
        self.click(self.click_btn)

