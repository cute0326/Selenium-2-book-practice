#coding:utf-8
__author__ = 'lenovo'
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time

#实际上，这个书上的例子，page类及LoginPage类的设计是有问题的，在父类中用子类才定义的东西，类外还有独立的函数，有违面向对象思想的且思路也不清晰
# 1. python 对这方面没有严格的检查机制
# 2. 虫师对面向对象的基础知识掌握的都不牢固，对面向对象也就是依葫芦哦画瓢# 的水平。
# 3. 类的分层思想不好，和页面有相关的信息分散得到处都是。用户调用的时候还要设置一些诸如 FireFox 之类可以抽取出来的公共信息。

# 基础类
class Page(object):
    '''基础类，用于页面对象类的继承'''

    driver = webdriver.Firefox()
    base_url = 'https://mail.qq.com'  # 整个网站的首页，跟目录   这个变量就是self.login_url啊
    special_url = '/'     # 对应各个子类要测试的子目录

    def __init__(self):
        self.timeout = 30 # __init__也可以为空的

#以下数据都是利用的初始化函数初始化之后的数据。
    def on_page(self):
        return self.driver.current_url == (self.base_url + self.special_url)

    def _open(self):
        target_url = self.base_url + self.special_url
        self.driver.get(target_url)
        # print('current_url is %s' %self.driver.current_url)
        # print('target_url is %s' %target_url)
        assert self.on_page(),'did not on the page'

    def open(self):
        self._open()

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    #driver定义到page类中了，那么相应的就得设计个退出driver的函数
    def driver_quit(self):
        self.driver.quit()

# 针对特定页面的测试类：有和页面相关的测试数据  这里使用的用户名需要与邮箱首页该账户实际显示的用户名一致（即QQ/（个性）邮箱/手机  ）
class LoginPage(Page):
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



#数字驱动测试
if __name__ == '__main__':

    #这里user也可以循环从文件读取，然后调用test_with_user_password
    user = "cute0326@qq.com"
    password = 'qinagW211.282.13'

    login_page = LoginPage()
    login_page.test_user_login(user,password)
