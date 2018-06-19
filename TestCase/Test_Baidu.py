#!/usr/bin/python3
# -*- coding: utf-8 -*-
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Email   : 944921374@qq.com

import unittest
from Pages.BaiduPage import BaiduPage
from Base.BrowserDriver import BrowserDriver

class BaiduCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = BrowserDriver(cls)
        cls.driver = driver.openbrowser(cls)

    def setUp(self):
        pass

    def test_baidu1(self):
        baidu = BaiduPage(self.driver)
        baidu.input_baidu_text('selenium')
        baidu.click_baidu_btn()
        baidu.get_screent_img()
        try:
            self.assertIn('selenium',self.driver.title())
            print('test pass')
        except Exception as e:
            print('test fail',format(e))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        pass

