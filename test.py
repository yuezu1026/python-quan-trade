# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import requests
from time import sleep
 
 
def getTick():
    url = "http://hq.sinajs.cn/list=sz000564"
    headers={'Referer':'https://finance.sina.com.cn/'}
    page = requests.get(url,headers=headers)
    
    
    stock_info = page.text
    mt_info = stock_info.split(",")
    
    last = float(mt_info[3])
    trade_datetime = mt_info[30] + ' '+ mt_info[31]
    
    tick = (last,trade_datetime)
    return tick
 
while True:
    last_tick = getTick()
    print(last_tick)
    sleep(3)
