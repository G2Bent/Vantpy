#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json

#使用post请求方式对手机号码进行删除请求
#举个栗子：删除测试服务器上的手机号码
def Dele(phone):
    url = 'http://112.74.29.84:***/api/User/deleteuser'
    teph = {'phone':phone}
    headers = {'content-type': 'application/json'}
    r = requests.post(url,json=teph,headers=headers)
    token_str = r.text
    token_dict = json.loads(token_str)
    if token_dict['success']==True:
        return True
    else:
        return False

#test
r = input("请输入手机号码:",)
print(Dele(r))
