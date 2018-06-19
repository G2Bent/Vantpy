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
        name_path = file_path + '\yaml\\browser.yaml'
        with open(name_path, 'r') as f:
            temp = yaml.load(f.read())
        # 获取配置文件属性
        brow = temp['brwserType']['browserName']
        browser = brow
        logger.info("选择的浏览器为: %s 浏览器" % browser)
        ur = temp['testUrl']['URL']
        url = ur
        logger.info("打开的URL为: %s" % url)
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("启动火狐浏览器")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("启动谷歌浏览器")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("启动IE浏览器")

        driver.get(url)
        logger.info("打开URL: %s" % url)
        driver.maximize_window()
        logger.info("全屏当前窗口")
        driver.implicitly_wait(5)
        logger.info("设置5秒隐式等待时间")
        return driver

    def quit_browser(self):
        logger.info("关闭浏览器")
        self.driver.quit()

