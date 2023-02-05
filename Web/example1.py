# -*- cording：utf-8 -*-
"""
@time:2023/01/07
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
driver=webdriver.Chrome()
driver.get("https://admin.test.jindiandan.cn/login/")
driver.find_element(By.XPATH,'//*[@id="app"]/div/form/div[2]/div/div/input').send_keys('yangchengchen')
sleep(5)

