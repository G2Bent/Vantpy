#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os.path
from selenium import webdriver
from Base.logger import Logger
import time

logger = Logger(logger="BrowserDriver").getlog()

class BrowserDriver(object):
    path = os.path.dirname(os.path.abspath('.'))#这是获取相对路径的方法
    chrome_driver_path = path + '/driver/chromedriver.exe'
    ie_driver_path = path + '/driver/IEDriverServer.exe'

    def __init__(self,driver):
        self.driver = driver

    def openbrowser(self,driver):
        # #读取配置文件
        # config = ConfigParser()
        # file_path = os.path.dirname(os.path.abspath('.'))+'\conf\config.ini'
        # config.read(file_path)

        #获取配置文件属性
        # browser = config.get("brwserType","browserName")
        browser = "Chrome"
        logger.info("You had select %s browser." % browser)
        # url = config.get("testUrl","URL")
        url = "https://www.baidu.com"
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
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        time.sleep(5)
        return driver

    def quit_browser(self):
        logger.info("Quit the browser.")
        self.driver.quit()

