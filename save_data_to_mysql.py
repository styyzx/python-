# coding:utf-8
 
import tushare as ts
import pymysql
import numpy as np
 
ts.set_token('你的接口TOKEN')
 
pro = ts.pro_api()
#调用trade_cal接口，设置起始日期和终止日期
data = pro.query('trade_cal', start_date='20190101', end_date='20201231', fields='cal_date,is_open,pretrade_date')
print(data)
 
dataset = np.array(data)
datalist = dataset.tolist()
 
# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306, user='mysql用户名', passwd='mysql密码', db='tushare', charset='utf8mb4')
 
 
cursor = db.cursor()
# SQL 插入语句
sql = "INSERT INTO trade_cal (cal_date,is_open,pretrade_date) VALUES (%s,%s,%s)"
 
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