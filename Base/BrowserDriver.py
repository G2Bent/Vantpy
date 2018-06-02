#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Email   : 944921374@qq.com

import os.path
from selenium import webdriver
from Base.logger import Logger
import yaml

logger = Logger(logger="BrowserDriver").getlog()

class BrowserDriver(object):
    path = os.path.dirname(os.path.abspath('.'))#这是获取相对路径的方法
    chrome_driver_path = path + '/driver/chromedriver.exe'
    ie_driver_path = path + '/driver/IEDriverServer.exe'

    def __init__(self,driver):
        self.driver = driver

    def openbrowser(self,driver):
        #读取配置文件
        file_path = os.path.dirname(os.getcwd())
        name_path = file_path + '\conf\config.yaml'
        with open(name_path, 'r') as f:
            temp = yaml.load(f.read())

        # 获取配置文件属性
        brow = temp['brwserType']['browserName']
        browser = brow
        logger.info("You had select %s browser." % browser)
        ur = temp['testUrl']['URL']
        url = ur
        logger.info("The test url is: %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(5)
        logger.info("Set implicitly wait 5 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Quit the browser.")
        self.driver.quit()

