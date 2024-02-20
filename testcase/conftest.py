# -*- coding: utf-8 -*-
# Time:2024/2/17 13:01
# Author:张柘
# File:conftest.py
# Desc:功能读取

import pytest
import yaml
import requests
from config.config import yaml_path


# 读取文件内容函数
def get_yaml_value(yamlfile, module=None, case_id=None):
    """
    :param yamlfile:
    :param module:
    :param case_id:
    :return:
    获取yaml文件的内容，包括req_url，Content-Type, data, expectation
    """
    data_list = []
    with open(yamlfile, 'r', encoding='utf-8') as file:
        content = file.read()
        print(type(content))
        data = yaml.safe_load(content)

    # 根据用户传入的 module 和 case_id 的值来决定读取什么范围的值
    if module == None and case_id == None:
        return data
    elif module != None and case_id == None:
        for values in data["NewBee"]:
            if module == values["module"]:
                data_list.append(values)
        return data_list
    elif case_id != None and module == None:
        for values in data["NewBee"]:
            if case_id == values["case_id"]:
                data_list.append(values)
        return data_list
    else:
        for values in data["NewBee"]:
            if case_id == values["case_id"]:
                data_list.append(values)
        return data_list


def send_request(method, url, data=None, headers=None):
    if data == None and headers == None:
        r = requests.request(method=method, url=url)
    else:
        r = requests.request(method=method, url=url, data=data, headers=headers)
    return r.text


# @pytest.fixture(scope='session')
def get_token(data):
    import json
    values = json.dumps(data)
    token1 = requests.post(url='http://47.99.134.126:28019/api/v1/user/login',
                           headers={'Content-Type': 'application/json'}, data=values)
    token_value = json.loads(token1.text)['data']
    return token_value


# if __name__ == '__main__':
#     a = get_yaml_value(yaml_path, case_id='api_01')
#     # print(a[0])
#     # print(type(a[0]))
#     token = get_token(a[0]['data'])
#     print(token)
