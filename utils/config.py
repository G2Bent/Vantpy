#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
读取配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。
"""
import os
from utils.readFile import YamlReader

# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'data', 'browser.yaml')
print(CONFIG_FILE)
# ELEMENT_PATH = os.path.join(BASE_PATH,'data','elements.yaml')
# CASE_PATH = os.path.join(BASE_PATH,'data','testcase.yaml')
# INTERFACE_PATH = os.path.join(BASE_PATH,'data','interface.yaml')
# DATA_PATH = os.path.join(BASE_PATH, 'data')
# DRIVER_PATH = os.path.join(BASE_PATH, 'drivers','chromedriver.exe')
# LOG_PATH = os.path.join(BASE_PATH, 'logs')
# REPORT_PATH = os.path.join(BASE_PATH, 'report')
# SCREENSHOTS_PATH = os.path.join(BASE_PATH,"screenshots",'')
# EXE_PATH = os.path.join(BASE_PATH,'test','Autolt','test1.jpg')
# EXCEL_PATH = os.path.join(BASE_PATH,'test','configSQL','')

# ,element = ELEMENT_PATH,case_data = CASE_PATH,
#                  interface_data = INTERFACE_PATH,chrome = DRIVER_PATH,screenshot = SCREENSHOTS_PATH,
#                  excel = EXCEL_PATH
class Config:
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data
        # print(self.config)
        # self.elements = YamlReader(element).data
        # self.case_data = YamlReader(case_data).data
        # self.interface_data = YamlReader(interface_data).data
        # self.exe_ptah = EXE_PATH
        # self.driver_pt = chrome
        # self.screen_shot = screenshot
        # self.excel_pt = excel


    def get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(element)

#     def get_ele(self,element,index = 0):
#         return self.elements[index].get(element)
#
#     def get_case_data(self,element,index = 0):
#         return self.case_data[index].get(element)
#
#     def get_inter_data(self,element,index = 0):
#         return self.interface_data[index].get(element)
#
#     def exe_data(self):
#         return self.exe_ptah
#
#     def driver_ptah(self):
#         return self.driver_pt
#
#     def screen_shot_path(self):
#         return self.screen_shot
#
#     def get_excel(self,file_name):
#         file_pt = self.excel_pt+"%s.xlsx"%file_name
#         return file_pt
# #
if __name__ == '__main__':
    c = Config()
    print(c.get("brwserType").get("browserName"))
    # print(c.get_ele('URL').get('url'))
    # print(c.exe_data())
    # print(c.screen_shot_path())
    # print(c.get_excel("user"))
    # print(c.driver_ptah())