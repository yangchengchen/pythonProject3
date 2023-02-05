# -*- cording：utf-8 -*-
"""
@time:2023/01/07
@Function:请输入模块功能描述
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
class WebKey:
    def __int__(self):
        self.driver=webdriver.Chrome()
    def openbrowser(self,br='gc'):
        if br=='gc':
            self.driver= webdriver.Chrome()
        elif br=='ff':
            self.driver=webdriver.Firefox()
        elif br=='ie':
            self.driver=webdriver.Ie()
        else:
            print('浏览器暂时不支持')
            pass
    def geturl(self,locator=None):
        self.driver.get(locator)
        self.driver.implicitly_wait(10)
    def click(self,locator=None):
        self.driver.find_element(By.XPATH,locator).click()
    def input(self,locator=None,value=None):
        self.driver.find_element(By.XPATH,locator).send_keys(value)
    def quit(self):
        self.driver.quit()