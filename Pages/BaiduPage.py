#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from Base.Selenium2 import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import *

class BaiduPage(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    search_loc = (By.XPATH,'//*[@id="kw"]')#定位百度文本框
    click_btn = (By.XPATH,'//*[@id="su"]')#定位百度按钮
    # input_box = "id=>kw"
    # search_submit_btn = "xpath=>//*[@id='su']"

    # 操作
    # 通过集成覆盖（overriding）方法:如果子类和父类的方法名相同，优先用子类自己的方法
    # 打开网页
    def open(self):
        # 调用selenium2中的_open方法打开链接
        self._open(self.base_url,self.pagetitle)

    def input_text(self,text):
        self.send_keys(self.search_loc,text)

    def click_baidu_btn(self):
        self.click(self.click_btn)