# coding=utf-8

import pandas as pd
import tushare as ts
from sqlalchemy import create_engine

from mysql_tables_structure import Base
import mysql_functions as mf

# 创建数据库引擎
engine = create_engine('mysql://root:123456@127.0.0.1/tushare?charset=utf8mb4')
conn = engine.connect()

# 创建mysql所有表结构
Base.metadata.create_all(engine)

# 连接 tushare
ts.set_token('b072d98ad9c6b41cb816bee74cc36646a0a0fbd5fb404b5c58b04e70')
pro = ts.pro_api()

# 股票列表
mf.update_stock_basic(engine, pro, 3, 2)


## https://www.52pojie.cn/thread-1073645-1-1.html
