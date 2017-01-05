# coding:utf-8
__author__ = 'lenovo'

from selenium.webdriver import Remote
from selenium import webdriver

def browser():
    dr = webdriver.Firefox()
    return dr

if __name__ == "__main__":
    dr = browser()
    dr.get('http://www.baidu.com')
    dr.quit()