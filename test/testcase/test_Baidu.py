#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Email   : 944921374@qq.com

import unittest
import sys
sys.path.append('../')
from test.page.BaiduPage import BaiduPage
from test.testcase.case_modle import *

class BaiduCase(model):

    def test_baidu(self):
        baidu = BaiduPage(self.driver)
        baidu.input_baidu_text('selenium')
        baidu.click_baidu_btn()
        # baidu.get_screent_img("baidu")
        self.assertIn('selenium',self.driver.title)
        # self.assertIn("sss",self.driver.title)
