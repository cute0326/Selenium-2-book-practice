# -*- coding:utf -8-*-

from calculator import Count
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        print('test.py 好强大')

    def tearDown(self):
        print('执行结束')

class TestAdd(MyTest):
    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
        # print('test_add one')

    def test_add2(self):
        j = Count(41,76)
        self.assertEqual(j.add(),117)
        # print('test_add2')

class TestSub(MyTest):

    def test_sub(self):
        j = Count(2,3)
        self.assertEqual(j.sub(),-1)
        # print('test sub one')

    def test_sub2(self):
        j = Count(71,46)
        self.assertEqual(j.sub(),25)
        # print('test sub2')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestAdd('test_add'))
    suite.addTest(TestSub('test_sub2'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
