__author__ = 'lenovo'

from selenium.webdriver import Remote

from time import sleep

#Remote的构造
# 第一种方法：
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# dr = Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)

# 第二种方法：
dc = {'browserName':'firefox','version':'','platform':'ANY',"javascriptEnabled": True, "marionette": False,}
#firefox 用remote就是不行，总是提示executable_path没有设定，看来是remote在初始化的时候针对firefox的时候忘记设置这个了。
#查看了一下firefox的webdriver，里面确实是有executable_path="geckodriver"，看来是selenium3的remote对firefox代码编有bug
#
dr = Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=dc)
dr.get('http://www.baidu.com')

dr.find_element_by_id('kw').send_keys('selenium')
dr.find_element_by_id('su').click()

sleep(3)

dr.quit()