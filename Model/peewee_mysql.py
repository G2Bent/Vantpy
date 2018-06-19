#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Vant
# @Email:944921374@qq.com
from peewee import *
import datetime
db = MySQLDatabase('test',host='127.0.0.1',port=3306,user='root',passwd='root')
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Users(BaseModel):
    username = CharField(unique=True)

class Tweet(BaseModel):
    user = ForeignKeyField(Users,related_name='tweets')
    message = TextField()
    create_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)

if __name__ == "__main__":
    #创建表
    # Users.create_table()#创建user表
    # Tweet.create_table()#创建Tweet表
    #添加数据
    # user = Users.create(username = 'tom')
    # Tweet.create(user=user,message = '这是一段文字')
    # Tweet.create(user_id = 1,message = '这是第二段文字')
    #查询数据
    t = Tweet.get(message='这是一段文字')
    print(t.user_id)
    print(t.create_date)
    print(t.is_published)
    #根据用户查询对应的所有数据
    ts = Tweet.filter(user_id = 1)
    for i in ts:
        print(i.message)
    
