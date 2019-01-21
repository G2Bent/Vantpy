#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from test.common.BrowserDriver import BrowserDriver
from test.page.login_page import *
from test.page.custom_page import *
from utils.config import Config
from time import sleep
from test.page.SubContractorPage import sub_contractor_page
class model(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        c = Config()
        username = c.get_case_data('login').get('username')
        password = c.get_case_data('login').get('password')
        driver = BrowserDriver(cls)
        cls.driver = driver.openbrowser(cls)


    def setUp(self):
        pass

    def teardown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()