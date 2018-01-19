#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import * #导入所有的异常类
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Pyse(object):
    original_window = None
    def __init__(self,driver,base_url,pagetitle):
        """
        :param driver:打开浏览器驱动
        :param base_url:输入测试url
        :param pagetitle:输入页面title
        """
        self.driver = driver
        self.base_url = base_url
        self.pagetitle = pagetitle


    def browser(browser = "Chrome"):
        """打开浏览器函数，Firefox，chrome，IE，phantomjs
           默认Chrome浏览器
        """
        try:
            if browser == "Chrome":
                driver = webdriver.Chrome()
                return driver
            elif browser == "firefox":
                driver = webdriver.Firefox()
                return driver
            elif browser == "IE":
                driver = webdriver.Ie()
                return driver
            elif browser == "phantomjs":
                driver = webdriver.PhantomJS()
                return driver
            else:
                print("找不到驱动")
        except Exception as msg:
            print("%s" % msg)

    def on_page(self,pagetitle):
        return pagetitle in self.driver.title

    def _open(self,url,pagetitle):
        """
        打开页面，校验页面是否加载正确
        以单下划线_开头的方法，在使用import *时，该方法不会被导入，保证该方法为类私有的。
        """
        self.driver.get(url)
        self.driver.maximize_window()
        assert self.on_page(pagetitle),"打开页面失败%s"%url

    def open(self):
        """
        :return:调用_open()进行打开链接
        """
        self._open(self.base_url,self.pagetitle)
        self.driver.maximize_window()

    def find_element(self,*element):
        """
        重定义定位方法
        return self.driver.find_element(*element)
        """
        try:
            WebDriverWait(self.driver,30).until(EC.visibility_of_all_elements_located(element))
            return self.driver.find_element(*element)
        except:
            print("页面元素未能找到%s"%self,element)

    def find_elements(self,*element):
        """
        重定义定位方法
        return self.driver.find_element(*element)
        """
        try:
            WebDriverWait(self.driver,30).until(EC.visibility_of_all_elements_located(element))
            return self.driver.find_elements(*element)
        except:
            print("页面元素未能找到%s"%self,element)

    def click(self,element):
        """点击操作"""
        element = self.find_element(element)
        element.click()

    def send_keys(self,element,text):
        """发送文本"""
        element = self.find_element(element)
        element.clear()
        element.send_keys(text)

    def move_to_element(self, element):
        '''
        鼠标悬停操作
        Usage:
        element = ("id","xxx")
        driver.move_to_element(element)
        '''
        element = self.find_element(element)
        ActionChains(self.driver).move_to_element(element).perform()

    def back(self):
        """
        浏览器返回窗口
        """
        self.driver.back()

    def forward(self):
        """
        浏览器前进下一个窗口
        """
        self.driver.forward()

    def close(self):
        """
        关闭浏览器
        """
        self.driver.close()

    def quit(self):
        """
        退出浏览器
        """
        self.driver.quit()

    def get_title(self):
        '''获取title'''
        return self.driver.title

    def get_text(self, element):
        '''获取文本'''
        element = self.find_element(element)
        return element.text

    def get_attribute(self, element, name):
        '''获取属性'''
        element = self.find_element(element)
        return element.get_attribute(name)

    def js_execute(self, js):
        '''执行js'''
        return self.driver.execute_script(js)

    def js_focus_element(self, element):
        '''聚焦元素'''
        target = self.find_element(element)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        '''滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def select_by_index(self, element, index):
        '''通过索引,index是索引第几个，从0开始'''
        element = self.find_element(element)
        Select(element).select_by_index(index)

    def select_by_value(self, element, value):
        '''通过value属性'''
        element = self.find_element(element)
        Select(element).select_by_value(value)

    def select_by_text(self, element, text):
        '''通过文本值定位'''
        element = self.find_element(element)
        Select(element).select_by_value(text)

    def is_text_in_element(self,element,text,timeout=10):
        """判断文本在元素里，没定位到元素返回False，定位到元素返回判断结果布尔值"""
        try:
            result = WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element(element,text))
        except TimeoutException:
            print("元素没有定位到:"+str(element))
            return False
        else:
            return result

    def is_text_in_value(self,element,value,timeout = 10):
        '''
        判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
        result = driver.text_in_element(element, text)
        '''
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(
                EC.text_to_be_present_in_element_value(element, value))
        except TimeoutException:
            print("元素没定位到：" + str(element))
            return False
        else:
            return result

    def is_title(self, title, timeout=10):
        '''判断title完全等于'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout=10):
        '''判断title包含'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(title))
        return result

    def is_selected(self, element, timeout=10):
        '''判断元素被选中，返回布尔值,'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_to_be_selected(element))
        return result

    def is_selected_be(self, element, selected=True, timeout=10):
        '''判断元素的状态，selected是期望的参数true/False
        返回布尔值'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_selection_state_to_be(element, selected))
        return result

    def is_alert_present(self, timeout=10):
        '''判断页面是否有alert，
        有返回alert(注意这里是返回alert,不是True)
        没有返回False'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.alert_is_present())
        return result

    def is_visibility(self, element, timeout=10):
        '''元素可见返回本身，不可见返回Fasle'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located(element))
        return result

    def is_invisibility(self, element, timeout=10):
        '''元素可见返回本身，不可见返回True，没找到元素也返回True'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.invisibility_of_element_located(element))
        return result

    def is_clickable(self, element, timeout=10):
        '''元素可以点击is_enabled返回本身，不可点击返回Fasle'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_to_be_clickable(element))
        return result

    def is_located(self, element, timeout=10):
        '''判断元素有没被定位到（并不意味着可见），定位到返回element,没定位到返回False'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(element))
        return result