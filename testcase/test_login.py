# -*- coding: utf-8 -*-
# Time:2024/2/17 13:01
# Author:张柘
# File:test_login.py
# Desc:
import json
import allure
from testcase import conftest
from config.config import yaml_path


@allure.feature('登录接口测试')
class TestLogin:
    def test_login(self):
        data_values = conftest.get_yaml_value(yaml_path, case_id="api_01")[0]
        # print(type(data_value))
        # print(data_value)
        url = data_values['req_url']
        data = data_values['data']
        method = data_values['req_method']
        header = data_values['header']
        expectation = dict(data_values['expectation'])
        exp = list(expectation)
        resps = conftest.send_request(method, url, data, header)
        resp = list(json.loads(resps))
        assert exp == resp, '测试成功'

# if __name__ == '__main__':
#     TestLogin().test_login()
