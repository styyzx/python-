# coding:utf-8

import tushare as ts
import pymysql
import numpy as np
import datetime
import time
import pandas as pd
import sys

import chinese_calendar

ts.set_token('b072d98ad9c6b41cb816bee74cc36646a0a0fbd5fb404b5c58b04e70')
pro = ts.pro_api()

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='tushare', charset='utf8mb4')
cursor = db.cursor()

sql = "select ts_code,pct_chg,vol_925,vol_925_ratio from stock_daily_2021_11_18 where vol_925_ratio > 0.01 order by " \
      "vol_925_ratio desc "
cursor.execute(sql)
print("cursor.excute:", cursor.rowcount)

# for each in cursor.fetchall():
#     print(each)
    

import datetime


def getYesterday(today):
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday

def getLastWorkDay(today):
    yesterday = getYesterday(today)
    while chinese_calendar.is_workday(yesterday) == False:
        yesterday = getYesterday(yesterday)
    return yesterday

today = datetime.date.today()
print (chinese_calendar.is_workday(getYesterday(today)))
#print(getYesterday().strftime("%Y%m%d"))
print(getLastWorkDay(today))
