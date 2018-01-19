#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
from openpyxl import load_workbook

wb = load_workbook("baidu.xlsx")
sheet = wb.get_sheet_by_name("Sheet1")

def GBK2312():
    """
       这里使用的是6000字汉字，用来被调用的方法
       :return: 返回随机汉字，陌生字相对会比较少
    """
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x}{body:x}'
    str = bytes.fromhex(val).decode('gb2312')
    return str

def String(Len):
    """
        生成随机汉字，用来被调用的方法
        :param num:调用获取汉字的方法，返回定义的个数
        :return:
        """
    s = ''
    for i in range(Len):
        s = s + GBK2312()
    return s

def RangeStr():
    """
    :return:返回自定义的字符长度
    """
    Str = String(4)
    return Str

def StrXlsx():
    """
    :return:从excel文件中读取数据
    """
    text = sheet['C']
    for i in random.choices(text):
        return i.value

def UrlXlsx():
    """
    :return:从excel中读取url
    """
    url = sheet['B']
    for i in url:
        return i.value
def titleXlsx():
    """
    :return:从文件中读取标题
    """
    title = sheet['A']
    for i in title:
        return i.value
