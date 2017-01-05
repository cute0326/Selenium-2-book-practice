# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from Login import Login

class LoginTest():

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get('https://mail.qq.com/')

    def test_admin_login(self):
        username = '3918747@qq.com'
        password = "qiangW211.282.13"
        Login().user_login(self.driver,username,password)
        sleep(5)
        Login().user_logout(self.driver)

    def test_guest_login(self):
        username = 'xxx'
        password = 'xxxx'
        Login.user_login(self.driver, username, password)
        sleep(5)
        Login().user_logout(self.driver)

LoginTest().test_admin_login()
# LoginTest().test_guest_login()


