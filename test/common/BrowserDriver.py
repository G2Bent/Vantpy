#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Email   : 944921374@qq.com

from selenium import webdriver
from utils.logger import Logger
from selenium.webdriver.chrome.options import Options
from utils.config import Config

logger = Logger(logger="BrowserDriver").getlog()

class BrowserDriver(object):
    path = './drivers/'#这是获取相对路径的方法
    chrome_driver_path = path + 'chromedriver.exe'
    ie_driver_path = path + '/driver/IEDriverServer.exe'

    def __init__(self,driver):
        self.driver = driver
        self.c = Config()

    def openbrowser(self,driver):
        browser = self.c.get("brwserType").get("browserName")
        logger.info("选择的浏览器为: %s 浏览器" % browser)
        url = self.c.get('ptahUrl').get('URL')
        logger.info("打开的URL为: %s" % url)
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("启动火狐浏览器")
        elif browser == "Chrome":
            chrome_options = Options()
            chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
            chrome_options.add_argument('--start-maximized')  # 指定浏览器分辨率
            chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
            # chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
            chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('lang=zh_CN.UTF-8')
            driver = webdriver.Chrome(options=chrome_options)

            # driver = webdriver.Chrome(self.c.driver_ptah()) #用于Windows系统加载驱动使用

            # driver = webdriver.Chrome() #用于linux系统加载驱动使用
            logger.info("启动谷歌浏览器")
        elif browser == "IE":
            driver = webdriver.Ie(self.c.driver_ptah())
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

