

import binance
import requests
import time
import hashlib
import hmac


from binance.error import ClientError
from binance.lib.utils import config_logging
from binance.spot import Spot as Client
from binance.client import Client
from datetime import datetime


api_key = ''#############自己的API都在 ‘’里填写
api_secret = ''####################自己的ASCERET都在 ‘’里填写
baseurl='https://api2.binance.com'
client = Client(api_key, api_secret)






def wait_for_market_open():
    target_time_str = '2023-10-17 13:22:00'  ###################### 开盘时间必须要改
    target_time_dt = time.strptime(target_time_str, "%Y-%m-%d %H:%M:%S")

    current_time = time.localtime()
    if current_time > target_time_dt:
        target_time_dt = time.localtime(time.time() + 86400)

    wait_seconds = (time.mktime(target_time_dt) - time.time())
    print(f"等待 {wait_seconds} 秒直到开盘时间")
    time.sleep(wait_seconds)

def buy_max_quantity():

    symbol='TIAUSDT'######################################### 这里要更改
    # 获取指定交易对的当前市价
    ticker = client.get_symbol_ticker(symbol=symbol)
    current_price = float(ticker['price'])

    # 计算可以购买的最大数量

    params = {
        'symbol': symbol,
        'side': 'BUY',
        'type': 'MARKET',




        'quoteOrderQty': '13'############这是购买的U的数量
    }

    response = client.create_order(**params)
    print(response)

# wait_for_market_open()
buy_max_quantity()
