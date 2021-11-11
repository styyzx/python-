# coding:utf-8

import tushare as ts
import pymysql
import numpy as np

ts.set_token('b072d98ad9c6b41cb816bee74cc36646a0a0fbd5fb404b5c58b04e70')

pro = ts.pro_api()

# 查询当前所有正常上市交易的股票列表
data = pro.stock_basic(exchange='', list_status='L',
                       fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
print(data)
dataset = np.array(data)
datalist = dataset.tolist()

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='tushare', charset='utf8mb4')

# 使用cursor()方法获取操作游标
cursor = db.cursor()
sql = "delete from stock_list"
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except Exception as e:
    print(e)
    # 如果发生错误则回滚
    db.rollback()
# 关闭游标
cursor.close()

cursor = db.cursor()
# SQL 插入语句
sql = "INSERT INTO stock_list (ts_code, symbol, name, area, industry, fullname, enname, market, exchange, curr_type, list_status, list_date, delist_date, is_hs) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

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

# 查询当前所有正常上市交易的股票列表
data1 = pro.stock_basic(exchange='', list_status='P',
                        fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
print(data1)
dataset1 = np.array(data1)
datalist1 = dataset1.tolist()

cursor = db.cursor()
try:
    # 执行sql语句
    cursor.executemany(sql, datalist1)
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