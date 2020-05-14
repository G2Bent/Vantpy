#!/usr/bin/env python
# -*- coding:utf-8 -*-

start =1
while start <= 10:
    #print(start)
     #如果是奇数，输出
     #否则不管
     #（译音：谈破）
     temp = start % 2
     #temp是余数，余数=0，偶数，否则：奇数
     if temp == 0:
         print(start)
     else:
         pass#pass什么都不执行(必须写，不写语法报错)
     start += 1

for i in range(1,11):
    resu = i%2
    if resu ==0:
        print(i,"是偶数")

