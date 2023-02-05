from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
def setup():
    print('用例开始')
def teardown():
    print('用例结束')

def test_01():
    print('01')

def test_02():
    print('02')