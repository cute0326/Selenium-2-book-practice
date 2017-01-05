from selenium import webdriver
from time import sleep

dr = webdriver.Ie()

dr.get('http://www.baidu.com')

dr.implicitly_wait(10)
dr.find_element_by_id('kw').send_keys('selenium')
dr.find_element_by_id('su').click()

sleep(3)

dr.quit()