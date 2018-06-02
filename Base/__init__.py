#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Time    : 2018/1/19 13:39
# @Email   : 944921374@qq.com
# @File    : __init__.py.py
# @Description:
import os
file_path = os.path.dirname(os.path.abspath('.'))+'\conf\config.ini'
print(file_path)
path = os.path.dirname(os.path.abspath('.'))#这是获取相对路径的方法
chrome_driver_path = path + '\driver\chromedriver.exe'
print(chrome_driver_path)