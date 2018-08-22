# -*- coding: utf-8 -*-
__author__ = 'qindongliang'

import pymysql
import time

def query(bracelet):
    # 打开数据库连接
    db = pymysql.Connect(
              host='120.79.101.51',
              port=3306,
              user='comma-admin',
              passwd='comma-admin',
              db='comma',
              charset='utf8',
            )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQLa 查询语句

    sql = "select bracelet_id from t_user_bracelet  where bracelet_id=%s "

    # try:
    # 执行SQL语句
    cursor.execute(sql,bracelet)
    #获取结果集
    results = cursor.fetchall()

    # print(results[0][0])


    # 关闭数据库连接
    db.close()

    return results[0][0]
# bracelet = 10000000
# bracelet += 1
# print(query(bracelet))
