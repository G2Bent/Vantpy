#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import time
import unittest
import sys
sys.path.append('../')
from HTMLTestRunner3 import HTMLTestRunner
from tomorrow import threads

#获取测试用例的路径

curpath = os.path.dirname(os.path.realpath(__file__))
casepath = os.path.join(curpath,'test','case')
reportpath = os.path.join(curpath,'report')

def add_case(case_path = casepath,rule= "test_*.py"):
    '''加载所有测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    return discover

@threads(3)
def run_case(all_case,report_path = reportpath,nth = 0):
    '''执行所有的用例，并把结果写入测试报告'''
    report_abspath = os.path.join(report_path,'result%s.html'%nth)
    fp = open(report_abspath,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title = "自动化测试报告，测试结果:",
                            description="用例执行情况:")
    runner.run(all_case)
    fp.close()

if __name__ == '__main__':
    #用例集合
    cases = add_case()
     #之前是批量执行，这里改成for循环执行
    for i , j in zip(cases,range(len(list(cases)))):
        run_case(i,nth = j)