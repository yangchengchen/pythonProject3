# -*- cording：utf-8 -*-
import requests
import json
def test_url():
    url='https://cdc.test.yuanting.cn/api/'
    return url
def login():
    url=test_url()
    data = requests.post(url+'passport/login',data={'account': "ycc000", 'password': "1111"})
    datas = data.json()
    datas = datas['data']['token']
    return datas
def post(url,datas):
    header=login()
    testurl=test_url()
    re=requests.post(testurl+url,data=datas,headers={"authorization":header})
    return re

#if __name__ == '__main__':

