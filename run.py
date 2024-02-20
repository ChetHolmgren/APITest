# -*- coding: utf-8 -*-
# Time:2024/2/17 13:05
# Author:张柘
# File:run.py
# Desc:
import subprocess

import pytest

pytest.main()
subprocess.call('allure generate ./result/temp -o ./result/report --clean', shell=True)
subprocess.call('allure open ./result/report', shell=True)
