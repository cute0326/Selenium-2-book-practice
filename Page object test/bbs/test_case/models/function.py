# coding:utf-8
__author__ = 'lenovo'

from selenium import webdriver
import os

#注意:
# 1. window系统的目录是这样的 "\"    D:\Python-test\mztestpro\bbs\report
# 2. pycharm处理过的为 "/"           D:/Python-test/mztestpro/bbs
# 3. 所以：如果是直接输入系统目录，可以用\\ print出来的为\ ， 如果是和系统的函数结果拼接，用“/”，这样就不会出现/和\ 混合的现象了

# 代码示范
# test = 'D:\\Python-test\\mztestpro\\bbs\\report'
# print(test)
 # print结果：D:\Python-test\mztestpro\bbs\report  若是pycharm函数处理过的，则为D:/Python-test/mztestpro/bbs/report/image/baidu.jpg

# base_dir = os.path.dirname(__file__)
# print(base_dir)
# print结果：D:/Python-test/mztestpro/bbs/test_case/models

def insert_img(driver,file_name):
    base_dir = os.path.dirname(__file__)
    print(__file__)
    base = base_dir.split('/test_case')[0]
    file_path = base + '/report/image/' + file_name
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://www.baidu.com')
    file_name = 'baidu.jpg'
    insert_img(driver,file_name)
    driver.quit()