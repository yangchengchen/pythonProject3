# -*- cording：utf-8 -*-
import time

import allure

from ddt.params import web
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from Web.webkeys import  WebKey
@allure.feature('原霆科技')
class Test_Commerce:
    def setup_class(self):
        self.web = WebKey()
        self.web.openbrowser()
    def teardown_class(self):
        time.sleep(4)
        self.web.quit()
    @allure.story('登录')
    @pytest.mark.parametrize('listcases',web()['loginPage'])
    def test_login(self,listcases):
        allure.dynamic.title(listcases['title'])
        allure.dynamic.description(listcases['description'])
        testcases = listcases['cases']
        for cases in testcases:
            listcase=list(cases.values())
            with allure.step(listcase[0]):
                func=getattr(self.web,listcase[1])
                values=listcase[2:]
                func(*values)
        # self.web.geturl('https://cdc.test.yuanting.cn/#/login')
        # self.web.input('//*[@id="app"]/div/form/div[2]/div/div/input','admin')
        # self.web.input('//*[@id="app"]/div/form/div[3]/div/div/input','1111')
        # self.web.click('//*[@id="app"]/div/form/button')
