# -*- coding:utf-8 -*-
__author__ = 'lenovo'

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()

driver.get('http://www.baidu.com')

source = driver.find_element_by_link_text('设置')

ActionChains(driver).move_to_element(source)
sleep(5)

ActionChains(driver).context_click(source).perform()

sleep(5)

target = driver.find_element_by_link_text('更多产品')

ActionChains(driver).move_to_element(target).perform()

sleep(5)

driver.quit()