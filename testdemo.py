# -*- coding: utf-8 -*-
# Time:2024/2/17 10:56
# Author:张柘
# File:testdemo.py
# Desc:接口自动化
import json
import requests

# 重要的数据转换
# json.loads() 将json转换为字典
# json.dumps() 将字典转换为json

# response_values = requests.request(method="GET", url="http://47.99.134.126:28019/api/v1/index-infos")
# value1 = response_values.text
# value2 = json.loads(value1)
# print(type(value2))

# # get()
# r = requests.get("http://47.99.134.126:28019/api/v1/index-infos")
# print(r.text)

# post()
payload = {
    "loginName": "18151104559",
    "passwordMd5": "E10ADC3949BA59ABBE56E057F20F883E"
}
header = {"Content-Type": "application/json"}

p = requests.post(data=json.dumps(payload), headers=header, url="http://47.99.134.126:28019/api/v1/user/login")

print(p.text)
# 要获取返回值response中的data值，即token值，首先要将返回值转换为字典格式，然后再进行搜索
# tokens = json.loads(p.text)['data']
# header = {"token": tokens}
# user_info = requests.get(headers=header, url="http://47.99.134.126:28019/api/v1/user/info")
# # print(user_info.text)
# # 添加断言
# expectation = json.loads(user_info.text)['message']
# assert expectation == 'SUCCESS'
