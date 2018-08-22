# -*- coding: utf-8 -*-
__author__ = 'qindongliang'

import pymysql
import time
import random


def query():
    # 打开数据库连接
    db = pymysql.Connect(
              host='120.79.101.51',
              port=3306,
              user='comma-admin',
              passwd='comma-admin',
              db='comma',
              charset='utf8',
            )

    # SQLa 查询语句


    i=0
    while i<200:
        i=i+1
        redeem_code = random.randint(0, 200)
        print(redeem_code)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        sql = "insert into `comma`.`t_redeem_code` (  `description`, `redeem_status`, `operator_id`, `tpl_coupon_id`, `user_coupon_id`, `start_time`, `user_id`, `redeem_code`, `end_time`, `duration`, `create_time`, `update_time`, `redeem_time`) values ( '1', '0', '1', '1', '0', '1524211002', '0','%s', '1629211002', '1', '1', '1524479177', '1')" % (redeem_code)

        # try:
        # 执行SQL语句
        cursor.execute(sql)
        db.commit()
        #获取结果集
        #results = cursor.fetchall()

        # print(results[0][0])


        # 关闭数据库连接
    db.close()

    #return results[0][0]
# bracelet = 10000000
# bracelet += 1
# print(query(bracelet))
query()
