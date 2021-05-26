# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     config
   Description :
   Author :       klook
   date：          2021/5/26
-------------------------------------------------
   Change Activity:
                   2021/5/26:
-------------------------------------------------
"""
__author__ = 'klook'

import configparser
import os

class Config:
    def __init__(self):
        BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        CONFIG_FILE = os.path.join(BASE_PATH, 'data', 'config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_FILE)

    def get(self,filename,key):
        conf = self.config.get(filename,key)
        return conf

    def path(self):
        BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        return BASE_PATH

if __name__ == '__main__':
    c = Config()
    # print(c.path())
    # print(c.get('browserType','browserName'))