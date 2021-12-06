from pytdx.hq import TdxHq_API
from pytdx.params import TDXParams
api = TdxHq_API()

import time


if api.connect('119.147.212.81', 7709):
    # ... same codes...
    data = api.get_security_bars(9, 0, '000628', 0, 1)  # 返回普通list
    #print(data)

    stock_list = api.get_security_list(1, 0)
    #print(stock_list)

    #minute_status = api.get_minute_time_data(1, '600300')
    # info = api.get_security_quotes( (0, '000628'))
    # print(info)
    info = api.get_transaction_data(TDXParams.MARKET_SH, '603779', 0, 30)
    # OrderedDict([('time', '14:38'), ('price', 23.03), ('vol', 38), ('num', 3), ('buyorsell', 1)]),

    time1 = ""
    vol1 = 0
    price1 = 0
    list_max_vol = []
    list_max_price = []
    list_max_price_vol = []
    for i in info :
        if time1 == i['time']:
           vol1 += i['vol']
           price1 = i['price']
        else:
            if len(list_max_price) == 0:
                list_max_price.append(price1)
                list_max_vol.append(vol1)
            elif list_max_price[len(list_max_price)-1] < price1 :

                list_max_price.append(price1)
                list_max_vol.append(vol1)
                if len(list_max_price_vol) == 0 :
                    list_max_price_vol.append((time1,price1,vol1))
                else:
                    if vol1 > list_max_price_vol[len(list_max_price_vol)-1][2] :
                        list_max_price_vol.append((time1, price1, vol1))
                        print(list_max_price_vol)

        time1 = i['time']
        vol1 = i['vol']
        print(list_max_price)
        #print(i)



    api.disconnect()

