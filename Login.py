# -*- coding: utf-8 -*-

__author__ = 'lenovo'

class Login():
    def user_login(self,driver,username,password):
        driver.switch_to.frame('login_frame')
        driver.find_element_by_link_text('帐号密码登录').click()
        driver.find_element_by_id('u').send_keys(username)
        driver.find_element_by_id('p').send_keys(password)
        driver.find_element_by_id('login_button').click()

    def user_logout(self,driver):
        driver.find_element_by_link_text('退出').click()
        driver.quit()