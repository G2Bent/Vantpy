#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json
#一、使用get方式请求,获取requests官网的源码
#respone =requests.get("http://cn.python-requests.org/zh_CN/latest/")
# print(respone.text)

#二、使用post方式请求,获取百度贴吧的源码
# respone = requests.post("https://tieba.baidu.com/")
# print(respone.text)

#三、传递url参数
#我们使用requests给我们提供的param关键字参数来传入参数
#url = 'http://httpbin.org/get'
#params = {'name':'dent','author':'vant'}
# params 支持列表作为值
#params = {'name': 'Good Time', 'author': ['Owl City', 'Carly Rae Jepsen']}
#respone = requests.get(url,params=params)
#print(respone.url)
#print(respone.text)

#四、构造请求头部
# url = "https://tieba.baidu.com/"
# headers = {
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
# #还可以设置其他字段
# }
# respone = requests.get(url,headers=headers)
# print(respone.url)
# print(respone.text)

#五、使用data参数提交数据
#data 参数通常结合 POST 请求方式一起使用。
# 如果我们需要用 POST 方式提交表单数据或者JSON数据，
# 我们只需要传递一个字典给 data 参数。

#提交表单数据
# url = 'http://httpbin.org/post'
# data = {
#     'user':'admin',
#     'pass':'admin'
# }
# respone = requests.post(url,data=data)
# print(respone.text)

#提交json请求
url = 'http://httpbin.org/post'
data = {
    'user':'admin',
    'pass':'admin'
}
#response = requests.post(url, data=json.dumps(data))
#这两个方式是一样的，下面的写法会更简单
respone = requests.post(url,json=data)
#print(respone.text)
print(respone.json())
print(respone.status_code)

#六、Cookie
url = "http://example.com/some/cookie/setting/url"
respone = requests.get(url)
print(respone.cookies)