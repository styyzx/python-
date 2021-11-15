# coding:utf-8

import tushare as ts
import pymysql
import numpy as np
import datetime
import time
import pandas as pd
import sys

ts.set_token('b072d98ad9c6b41cb816bee74cc36646a0a0fbd5fb404b5c58b04e70')
pro = ts.pro_api()

from pytdx.hq import TdxHq_API

api = TdxHq_API()
b_con = 0
if api.connect('119.147.212.81', 7709):
    b_con = 1

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='tushare', charset='utf8mb4')

# 使用cursor()方法获取操作游标
cursor = db.cursor()
sql = "delete from stock_daily_find"
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


# 查询当前所有正常上市交易的股票列表
data = pro.stock_basic(exchange='', list_status='L',
                       fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')

dataset = np.array(data)
stock_list = dataset.tolist()
print(stock_list)

#sql = "select cal_date from trade_cal where cal_date ='" + str(sys.argv[1]) + "' and is_open=1 order by cal_date"
#sql = "select cal_date from trade_cal where cal_date ='" + str('20211112') + "' and is_open=1 order by cal_date"

print("stock_list len= ", stock_list.__len__())

# for each in stock_list:
#print(datetime.datetime.strftime('20211112', "%Y%m%d"))
data = pro.daily(trade_date='20211112')
cursor = db.cursor()
datalist = np.array(data).tolist()
#sql = "insert into stock_daily( ts_code, trade_date, `open`, high, low, `close`, pre_close, `change`, pct_chg, vol, amount) values ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )"
sql = "insert into stock_daily_find( ts_code, trade_date, `open`, high, low, `close`, pre_close, `change`, pct_chg, vol, amount,vol_925_ratio) values ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )"

print(datalist.__len__())
info = api.get_security_quotes( (0, 300473))
print(info)

for data in datalist:
    if len(data) < 6 or float(data[2])==0:
        continue
    if ( (float(data[5]) - float(data[2])) / float(data[2]) >0.09 ) :
        #print(data)
        stock_code = data[0][0:6]
        parket_code = 1 if data[0][7:9]=='SH' else 0
        print(parket_code, stock_code)
        if data[0].__len__() < 6:
            continue
        info = api.get_security_quotes( (parket_code, stock_code))
        print(info[0]['reversed_bytes3'])
        data.append(str(float(info[0]['reversed_bytes3']) / float(data[9])))
        try:
            # 执行sql语句
            cursor.execute(sql, data)
            # 提交到数据库执行
            db.commit()
        except Exception as e:
            print(e)
            # 如果发生错误则回滚
            db.rollback()
      



api.disconnect()

    # try:
    #     # 执行sql语句
    #     cursor.executemany(sql, datalist)
    #     # 提交到数据库执行
    #     db.commit()
    # except Exception as e:
    #     print(e)
    #     # 如果发生错误则回滚
    #     db.rollback()