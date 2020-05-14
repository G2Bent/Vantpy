#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
import pandas as pd
from utils.config import Config

#打开数据库
class MysqlLib(object):
    def __init__(self, ip, user, password, db_name, charset='utf8'):
        try:
            self.ip1 = ip
            self.user = user
            self.password = password
            self.db_name = db_name
            self.char = charset

            self.MySQL_db = pymysql.connect(
                host=self.ip1,
                user=self.user,
                password=self.password,
                db=self.db_name,
                charset=self.char,
            )
            print('连接成功')
        except:
            print('Error:connect is error')

    def sql_exe(self, sql):
        cursor = self.MySQL_db.cursor()
        Mysql_sql = sql
        try:
            # 執行sql語句
            cursor.execute(Mysql_sql)
            self.MySQL_db.commit()
        except:
            print("Error:unable to fetch data")
            self.MySQL_db.close()
        self.MySQL_db.close()

    def create_table(self,tablename):
        #创建一张表
        cursor = self.MySQL_db.cursor()
        #如果表存在就先执行删除表
        try:
            cursor.execute("DROP TABLE IF EXISTS %s"%tablename)
            sql = """CREATE TABLE %s( 
                ID VARCHAR(100) NOT NULL,
                Name VARCHAR(30),
                Grade INT,
                AGE INT,
                GENDER VARCHAR(30))"""%tablename
            cursor.execute(sql)
            print("创建成功")
            return True
        except:
            print("创建失败")
            return False

    def into_sql(self):
        xl = Config().get_excel("user")
        df = pd.read_excel(xl,sheet_name="Sheet2")#sheetname不填默认为第一个sheet表
        #开始写入数据
        username = df.username
        cardnum = df.cardnum.astype(object)
        age = df.age.astype(object)
        gender = df.gender
        for i in range(len(df)):
            sql = "INSERT INTO user(USERNAME,CARDNUM,AGE,SEX) VALUES(%s,%s,%s,%s)"
            values = (username[i],cardnum[i],age[i],gender[i])
            cursor = self.MySQL_db.cursor()
            print(i,values)
            try:
                cursor.execute(sql,values)
                self.MySQL_db.commit()
                print('info success')
            except:
                print("Error: no date to into")
                self.MySQL_db.close()
        self.MySQL_db.close()

    def query_all_sql(self,name):
        cursor = self.MySQL_db.cursor()
        sql = "SELECT * FROM %s"%name
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                id = row[0]
                username = row[1]
                birthday = row[2]
                print('id:%s,username:%s,bithday:%s'%(id,username,birthday))
        except:
            print("Error: unable to fetch data")
        self.MySQL_db.close()

    def query_ont_sql(self,name,id):
        cursor = self.MySQL_db.cursor()
        sql = "SELECT * FROM %s WHERE s_id = %s"% (name,id)
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                id = row[0]
                username = row[1]
                birthday = row[2]
                print('id:%s,username:%s,bithday:%s' % (id, username, birthday))
        except:
            print("Error: unable to fetch data")
        self.MySQL_db.close()

    def update_sql(self,which,value,id):
        cursor = self.MySQL_db.cursor()
        sql = "UPDATE %s SET s_name ='%s' WHERE s_id=%s"%(which,value,id)
        try:
            cursor.execute(sql)
            self.MySQL_db.commit()
            print('Update success')
        except:
            print("Error:update data discover error")
            self.MySQL_db.rollback()
        self.MySQL_db.close()

    def del_sql(self,which,id):
        cursor = self.MySQL_db.cursor()
        sql = 'DELETE FROM %s WHERE s_id = %s'%(which,id)
        try:
            cursor.execute(sql)
            self.MySQL_db.commit()
            print('delete %s is success'%id)
        except:
            print('Error:delete is fail,please check your sql format')
            self.MySQL_db.rollback()
        self.MySQL_db.close()

    def alter_sql(self,which,value):
        cursor = self.MySQL_db.cursor()
        sqladd = """alter table %s add %s varchar(20) not null"""%(which,value)#添加列
        sqlchange = """alter table %s change %s VARCHAR(30) not NULL """%(which,value)#更改列
        sqldrop = """alter table %s drop %s"""%(which,value)#删除表
        sqlre = """alter table %s rename %s"""(which,value)#重命名表
        try:
            cursor.execute(sqladd)
            self.MySQL_db.commit()
        except:
            print("add alter fail ")
            self.MySQL_db.rollback()
        self.MySQL_db.close()

if __name__ == '__main__':

    p = ['127.0.0.1','root','','autotest']
    test = MysqlLib(p[0], p[1], p[2], p[3])
    print(test)
    # print(test.into_sql())
    # print(test.create_table('ch'))
    # print(test.query_all_sql('student'))
    # print(test.query_ont_sql("student",'02'))
    # print(test.update_sql('student','hel8o','03'))
    # print(test.del_sql('student','03'))
    # print(test.alter_sql('student','eng_name'))