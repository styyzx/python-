import requests
import json
import pymysql

class mysql_conn(object):
    # 魔术方法, 初始化, 构造函数
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1', user='root', password='abc123', port=3306, database='py1011')
        self.cursor = self.db.cursor()
    # 执行modify(修改)相关的操作
    def execute_modify_mysql(self, sql):
        self.cursor.execute(sql)
        self.db.commit()
    # 魔术方法, 析构化 ,析构函数
    def __del__(self):
        self.cursor.close()
        self.db.close()

headers = { # 使用抓包工具分析发送数据请求到json格式的cookie数据，这是此次动态抓取的重点
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

#获取可转债数据
url = 'https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=30&order=desc&orderby=percent&order_by=percent&exchange=CN&market=CN&industry=%E5%8F%AF%E8%BD%AC%E5%80%BA&type=convert&_=1637705549702'

response = requests.get(url,headers=headers)

res_dict = json.loads(response.text)
#print(res_dict)
dict_list = res_dict['data']['list']
list_size = res_dict['data']['count']
db ={}
print (list_size)
for list_item_dict in dict_list:
    # data_dict = json.loads(list_item_dict['data'])
    print(list_item_dict)
