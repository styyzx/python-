# coding:utf-8

import tushare as ts
import pymysql
import numpy as np
import datetime
import time
import pandas as pd
import sys
# 通达信接口
from pytdx.hq import TdxHq_API

api = TdxHq_API()

# tushare接口
ts.set_token('b072d98ad9c6b41cb816bee74cc36646a0a0fbd5fb404b5c58b04e70')
pro = ts.pro_api()

b_con = 0
if api.connect('119.147.212.81', 7709):
    b_con = 1

# 数据库连接
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='tushare', charset='utf8mb4')

import datetime
import chinese_calendar


def getYesterday(today):
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


def getLastWorkDay(today):
    yesterday = getYesterday(today)
    while chinese_calendar.is_workday(yesterday) == False:
        yesterday = getYesterday(yesterday)
    return yesterday


def execute_sql_str(sql_str):
    # 使用cursor()方法获取操作游标
    cursor_temp = db.cursor()
    # sql = "delete from stock_daily_find"
    try:
        # 执行sql语句
        cursor_temp.execute(sql_str)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        db.rollback()
    # 关闭游标
    cursor_temp.close()


def execute_sql_file(sql_path):
    cursor_temp = db.cursor()
    with open(sql_path, 'r+') as f:
        # every sql job last line marked;
        sql_list = f.read().split(';')[:-1]
        sql_list = [x.replace('\n', ' ') if '\n' in x else x for x in sql_list]
    for sql_item in sql_list:
        print(sql_item)
        try:
            cursor_temp.execute(sql)
            # 提交到数据库执行
            db.commit()
        except Exception as e:
            print(e)
            # 如果发生错误则回滚
            db.rollback()

    # 关闭游标
    cursor_temp.close()


# execute_sql_file('sql_file/daily_info.sql')

# info = api.get_security_quotes( (0, 300473))
# print(info)


from pytdx.params import TDXParams


def find_max_price_vod(data_fetch):
    for data in data_fetch:
        print(data)
        parket_code = TDXParams.MARKET_SH if data[7:9] == 'SH' else TDXParams.MARKET_SZ
        info = api.get_transaction_data(parket_code, data, 0, 30)
        # OrderedDict([('time', '14:38'), ('price', 23.03), ('vol', 38), ('num', 3), ('buyorsell', 1)]),

        time1 = ""
        vol1 = 0
        price1 = 0
        list_max_vol = []
        list_max_price = []
        list_max_price_vol = []
        for i in info:
            if time1 == i['time']:
                vol1 += i['vol']
                price1 = i['price']
            else:
                if len(list_max_price) == 0:
                    list_max_price.append(price1)
                    list_max_vol.append(vol1)
                elif list_max_price[len(list_max_price) - 1] < price1:

                    list_max_price.append(price1)
                    list_max_vol.append(vol1)
                    if len(list_max_price_vol) == 0:
                        list_max_price_vol.append((data,time1, price1, vol1))
                    else:
                        if vol1 > list_max_price_vol[len(list_max_price_vol) - 1][2]:
                            list_max_price_vol.append((data,time1, price1, vol1))
                            if len(list_max_price_vol) == 3:
                                list_max_price_vol.pop(0)
                                print ('------------------ congretolations ------------------ BUY BUY BUY!!! ', data)
                                print(list_max_price_vol)
                            print(list_max_price_vol)

            time1 = i['time']
            vol1 = i['vol']
            #print(list_max_price)


def execute_query(sql_str):
    temp_cursor = db.cursor()
    temp_cursor.execute(sql_str)
    print("查询到行数:", temp_cursor.rowcount)

    # for each in temp_cursor.fetchall():
    #     print(each)
    data_fetch = temp_cursor.fetchall()
    print (data_fetch)
    temp_cursor.close()
    return data_fetch


sql = "select ts_code from " + 'stock_daily_2021_11_19' + " where vol_925_ratio > 5 order by " \
                                                "vol_925_ratio desc "
execute_query(sql)
find_max_price_vod(('603779.SH','601018.SH'))

while 1 :
    find_max_price_vod(('603779.SH','601018.SH'))
    time.sleep(0.8)


api.disconnect()
