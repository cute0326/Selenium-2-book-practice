# coding:utf-8
__author__ = 'lenovo'

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base import Page
from time import sleep
from selenium import webdriver

class login(Page):
    '''QQ登录邮箱页面'''

    special_url = '/cgi-bin/loginpage'  # 对应测试类要测试的页面的url

    username_loc = (By.ID,'u')
    password_loc = (By.ID,'p')
    submit_loc = (By.ID,'login_button')
    frame_loc = 'login_frame' # 注意frame_loc 设置的特别之处，因为切换到frame不需要By.ID。他只接受ID一个参数，所以这里没有By.ID,否则传入参数多1
    dialog_loc = (By.LINK_TEXT,'帐号密码登录')
    check_user_loc = (By.ID,'useraddr')

    #action
    #在写自动化寻找元素的时候，先手动仔细寻找一下，否则很容易想当然，忽略某些步骤，导致元素找不到，不熟悉的报错分析起来好浪费时间。

    def switch_to_dialog(self):
        self.find_element(*self.dialog_loc).click()

    def switch_to_frame(self):
        # print('the len of the frame_loc is %d'% len(self.frame_loc))
        self.driver.switch_to.frame(self.frame_loc)
        #当frame只需要一个参数的时候，就不要加*了，否则单独的一个字符串会被解释成含有len(string)那么多个字母的tuple

    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()

    def check_user(self,username):
        text = self.find_element(*self.check_user_loc).text
        # print(text)
        assert(text == username),'用户名称不匹配，登录失败'


    # 针对特定测试创建的测试方法  ---> 把这些与特定测试类挂钩的函数都挪到测试类中去，这样比较统一。
    def test_user_login(self,username,password):
        '''测试获取的用户名，密码是否可以登录'''
        self.open()
        self.switch_to_frame()
        self.switch_to_dialog()
        self.type_username(username)
        self.type_password(password)
        self.submit()
        sleep(3)   # 需要sleep一下，否则定位不到邮箱的名字，因为邮箱的名字还没有更新出来呢。

if __name__ == '__main__':
    driver = webdriver.Firefox()
    test = login(driver)
    user = 'cute0326@qq.com'
    password = 'qiangW211.282.13'
    test.test_user_login(user,password)
