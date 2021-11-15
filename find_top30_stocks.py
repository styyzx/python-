# coding:utf-8

import tushare as ts
import pymysql
import numpy as np
import datetime
import time
import pandas as pd
import sys

from pytdx.hq import TdxHq_API
tdx_api = TdxHq_API()

ts.set_token('b072d98ad9c6b41cb816bee74cc36646a0a0fbd5fb404b5c58b04e70')
pro = ts.pro_api()

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
    sql = "insert into stock_daily( ts_code, trade_date, `open`, high, low, `close`, pre_close, `change`, pct_chg, vol, amount) values ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )"
    sql_find = "insert into stock_daily_find( ts_code, trade_date, `open`, high, low, `close`, pre_close, `change`, pct_chg, vol, amount,vol_925_ratio) values ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )"

    print(sql)
    b_con = 0;
    if tdx_api.connect('119.147.212.81', 7709):
        b_con = 1

    for data in datalist:
        if ( (float(data[5]) - float(data[2])) / float(data[2]) >0.09 ) :
            cur_vol = 0
            # ... same codes...
            minute_status = tdx_api.get_security_quotes(1 if str(data[0]).find('SH') > 0 else 0, data[0])
            # print(minute_status)
            data.append(str((float(data[5]) - float(data[2])) / float(data[9])))

            try:
                # 执行sql语句
                cursor.execute(sql_find, data)
                # 提交到数据库执行
                db.commit()
            except Exception as e:
                print(e)
                # 如果发生错误则回滚
                db.rollback()
        # else :
        #     print(data)
    if b_con == 1 :
        tdx_api.disconnect()



    # try:
    #     # 执行sql语句
    #     cursor.executemany(sql, datalist)
    #     # 提交到数据库执行
    #     db.commit()
    # except Exception as e:
    #     print(e)
    #     # 如果发生错误则回滚
    #     db.rollback()