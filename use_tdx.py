from pytdx.hq import TdxHq_API

api = TdxHq_API()


if api.connect('119.147.212.81', 7709):
    # ... same codes...
    data = api.get_security_bars(9, 0, '300437', 0, 1)  # 返回普通list
    print(data)

    stock_list = api.get_security_list(1, 0)
    print(stock_list)

    minute_status = api.get_minute_time_data(1, '600300')
    print(minute_status)
    api.disconnect()