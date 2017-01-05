from threading import Thread
from selenium import webdriver
from time import sleep,ctime

def test_baidu(host,browser):
    print('start"%s' %ctime())
    print(host, browser)

    dc = {}

    driver = webdriver.Remote(command_executor=host,desired_capabilities={'platform'})   #chrome的浏览器可以这样，但是firefox的这么做会有点问题。

    driver.get('https://www.baidu.com/')
    driver.find_element_by_id('kw').send_keys('selenium')
    driver.find_element_by_id('su').click()
    sleep(3)
    driver.quit()

if __name__ == '__main__':
    # lists = {'http://127.0.0.1:4444/wd/hub':'chrome','http://127.0.0.1:5555/wd/hub':'Firefox'}
    test_baidu('http://127.0.0.1:4444/wd/hub','firefox')
    # 若使用java -jar selenium-server-standalone-2.53.0.jar -role hub只启动hub，即使通过4444分配给server，此hub也是不自己运行代码的，需要有一个node代码才能顺利运行。
    # java -jar selenium-server-standalone-2.53.0.jar 则server是可以运行代码的。

    print('ends: %s:'%ctime())

