# 获取数据模块 get_data_func 函数，返回实时行情的DataFrame数据对象
import requests
import pandas as pd
from pandas import Series, DataFrame

import tushare as ts
import pymysql
import numpy as np

ts.set_token('b072d98ad9c6b41cb816bee74cc36646a0a0fbd5fb404b5c58b04e70')

pro = ts.pro_api()


# 请注意，随着交易合约的到期，品种代码字典需要隔断时间更新
# f_code = {'A2009': '豆一', 'B2009': '豆二', 'C2009': '玉米', 'M2009': '豆粕', 'Y2009': '豆油', 'OI2009': '菜油', 'RM2009': '菜粕',
#           'P2009': '棕油',
#           'JD2009': '鸡蛋', 'SR2009': '白糖', 'AP2010': '苹果', 'CJ2009': '红枣', 'SP2009': '纸浆', 'CF2009': '棉花',
#           'FG2009': '玻璃', 'MA2009': '甲醇',
#           'EG2009': '乙醇', 'PP2009': '丙烯', 'L2009': '乙烯', 'V2009': '氯乙', 'RU2009': '橡胶', 'BU2012': '沥青', 'FU2009': '燃油',
#           'ZC2009': '动煤',
#           'JM2009': '焦煤', 'J2009': '焦炭', 'SM2009': '锰硅', 'SF2010': '硅铁', 'AG2012': '沪银', 'AL2012': '沪铝', 'NI2010': '沪镍',
#           'PB2009': '沪铅',
#           'ZN2009': '沪锌', 'SN2009': '沪锡', 'HC2010': '卷板', 'RB2010': '螺纹'
#           }

# 查询当前所有正常上市交易的股票列表
data1 = pro.stock_basic(exchange='', list_status='L',
                        fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
print(data1)
dataset1 = np.array(data1)
datalist1 = dataset1.tolist()
stock_code_list = []
for name in datalist1:
    stock_code_list.append(name[0])

print(stock_code_list.__len__())

def get_data_func():
    #data_df = pd.DataFrame(index=['Time', 'Open', 'High', 'Low', 'Price'])
    data_df = []
    for name in stock_code_list:
        url = ('http://hq.sinajs.cn/list=' + name)
        resp = requests.get(url)  # 获取数据
        get_data = resp.text.split(',')  # 数据分解成list
        print(get_data)
        #data_list = [get_data[1], get_data[2], get_data[3], get_data[4], get_data[8]]  # 选取需要的数据
        #data_flist = list(map(float, get_data))  # 字符串转换成浮点数据
        #data_df.append(get_data)  # 将选取的数据列表逐个存入DataFrame

    return (data_df)


g = get_data_func()
print(g)
