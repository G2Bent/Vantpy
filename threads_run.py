#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver

# 测试用例
from time import sleep, ctime
import threading

from tomorrow import threads


def test_baidu(browser, search):
    print('start:%s' % ctime())
    print('browser:%s,' % browser)
    if browser == 'ie':
        driver = webdriver.Ie()
    elif browser == "chrome":
        driver = webdriver.Chrome('E:\1test\Vantpy\drivers\chromedriver.exe')
    elif browser == 'ff':
        driver = webdriver.Firefox()
    else:
        print("browser 参数有误，只能为ie ，ff，chrome")
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(search)
    driver.find_element_by_id("su").clear()
    sleep(2)
    driver.quit()


if __name__ == '__main__':
    # 启动参数（指定浏览器与百度收缩内容）
    lists = {'chrome': 'threading'}
    threads = []
    files = range(len(lists))

    # 创建线程
    for browser, search in lists.items():
        t = threading.Thread(target=test_baidu, args=(browser, search))
        threads.append(t)

    # 启动线程
    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()
    print('end:%s' % ctime())