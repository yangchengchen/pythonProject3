# -*- cording：utf-8 -*-
import os
import allure
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from ddt.params import workflow
from ddt.params import web
#pytest.main(['-s','Suites/test_example4.py','--reruns','2'])
pytest.main(['ddt/yuanting_test.py','--alluredir', '/Users/a00/PycharmProjects/pythonProject3/temp','-s'])
#os.system('allure generapwdte /Users/a00/PycharmProjects/pythonProject3/Suites/temp -o /Users/a00/PycharmProjects/pythonProject3/Suites/report')
#os.system('allure generate /Users/a00/PycharmProjects/pythonProject3/temp -o /Users/a00/PycharmProjects/pythonProject3/report --clean')

