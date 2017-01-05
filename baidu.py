# -*- coding: utf-8 -*-
__author__ = 'lenovo'

from selenium import webdriver
from time import sleep

search_text = ['python','中文','text']

for text in search_text:
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get('http://www.baidu.com')

    driver.find_element_by_id('kw').send_keys(text)
    sleep(2)
    driver.find_element_by_id('su').click()
    print(driver.current_url)

    sleep(4)
    driver.quit()