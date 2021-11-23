import requests

import pymongo
import json


# 数据库初始化
client = pymongo.MongoClient("localhost", 27017)
# 获得数据库
db = client.gupiao
# 获得集合
stu = db.lushen




headers = {
"Accept" : "application/json, text/javascript, */*; q=0.01",
"Accept-Encoding" : "gzip, deflate, br",
"Accept-Language" : "zh-CN,zh;q=0.9",
"cache-control" : "no-cache",
"Connection" : "keep-alive",
"Cookie" : "aliyungf_tc=AQAAALpBylKYjA4AsLc5cWOtI0XvXlDf; xq_a_token=229a3a53d49b5d0078125899e528279b0e54b5fe; xq_a_token.sig=oI-FfEMvVYbAuj7Ho7Z9mPjGjjI; xq_r_token=8a43eb9046efe1c0a8437476082dc9aac6db2626; xq_r_token.sig=Efl_JMfn071_BmxcpNvmjMmUP40; __utma=1.461614876.1522589407.1522589407.1522589407.1; __utmc=1; __utmz=1.1522589407.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_1db88642e346389874251b5a1eded6e3=1522589408; u=311522589410819; device_id=a570575343f72340971cbc6acbb00ba7; s=f314ecnpa7; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1522589950",
"Host" : "xueqiu.com",
"Referer" : "https://xueqiu.com/hq",
"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
"X-Requested-With" : "XMLHttpRequest"


   }






for i in range(1,185):
    url = 'https://xueqiu.com/stock/cata/stocklist.json?page='+str(i)+'&size=30&order=desc&orderby=percent&type=11%2C12&_=1522591974896'


    response = requests.get(url=url, headers=headers)
    # with open('aaa.text',) as f:
    #     response = f.read()
    data = json.loads(response.text)
    print(data)
    column =['symbol', 'name', 'current', 'chg', 'percent', 'last_close', 'open', 'high', 'low', 'volume', 'amount', 'market_capital', 'pe_ttm', 'high52w', 'low52w', 'hasexist']


    dict_ ={}
    for b in data['stocks']:
        num = 0
        for a in column:
            dict_[a] = b[num]
            num += 1



        stu.update({'symbol': dict_['symbol']}, dict(dict_), True)
#————————————————
#版权声明：本文为CSDN博主「半吊子Py全栈工程师」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/qq_26877377/article/details/79782746