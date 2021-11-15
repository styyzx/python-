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
db1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='tushare', charset='utf8mb4')
cursor = db1.cursor()

#sql = "select cal_date from trade_cal where cal_date ='" + str(sys.argv[1]) + "' and is_open=1 order by cal_date"
sql = "select cal_date from trade_cal where cal_date ='" + str('20211112') + "' and is_open=1 order by cal_date"
cursor.execute(sql)
print("cursor.excute:", cursor.rowcount)
for each in cursor.fetchall():
    print(datetime.datetime.strftime(each[0], "%Y%m%d"))
    data = pro.daily(trade_date=datetime.datetime.strftime(each[0], "%Y%m%d"))
    cursor = db.cursor()
    datalist = np.array(data).tolist()
    #sql = "insert into stock_daily( ts_code, trade_date, `open`, high, low, `close`, pre_close, `change`, pct_chg, vol, amount) values ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )"
    sql = "insert into stock_daily_find( ts_code, trade_date, `open`, high, low, `close`, pre_close, `change`, pct_chg, vol, amount, vol_925_ratio) values ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )"
    print(sql)
    for data in datalist:
        if ( (float(data[5]) - float(data[2])) / float(data[2]) >0.09 ) :
            #print(data)
            stock_code = data[0][0:6]
            parket_code = 1 if data[0][7:9]=='SH' else 0
            print(parket_code, stock_code)
            info = api.get_security_quotes( (parket_code, stock_code))
            print(info[0]['reversed_bytes3'])
            datalist.append(str(info[0]['reversed_bytes3']))
            try:
                # 执行sql语句
                cursor.execute(sql, datalist)
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