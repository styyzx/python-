# coding:utf-8

import tushare as ts
import pymysql
import numpy as np

ts.set_token('b072d98ad9c6b41cb816bee74cc36646a0a0fbd5fb404b5c58b04e70')

pro = ts.pro_api()
# 调用trade_cal接口，设置起始日期和终止日期
data = pro.query('trade_cal', start_date='20200101', end_date='2021112', fields='cal_date,is_open,pretrade_date')
print(data)

dataset = np.array(data)
datalist = dataset.tolist()

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='tushare', charset='utf8mb4')

cursor = db.cursor()
# SQL 插入语句
sql = "REPLACE INTO trade_cal (cal_date,is_open,pretrade_date) VALUES (%s,%s,%s)"

try:
    # 执行sql语句
    cursor.executemany(sql, datalist)
    # 提交到数据库执行
    db.commit()
except Exception as e:
    print(e)
    # 如果发生错误则回滚
    db.rollback()
# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()