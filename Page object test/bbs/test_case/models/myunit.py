# coding:utf-8
__author__ = 'lenovo'

from selenium import webdriver
from driver import browser   #技巧  1.不会单独调用myunit。 2.在其他模块调用myunit的时候不需要使用软添加，节省了大量的工作
# 但是看后来使用myunit的，也软添加了myunit的路径了，那么这里就直接写就好了，加个.反而没那么规则了。。。。。
import unittest
import os

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        print('I can work well')
        self.driver.quit()

    def test_add(self):
        pass
