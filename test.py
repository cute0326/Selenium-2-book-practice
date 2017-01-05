# -*- coding: utf-8 -*-
__author__ = 'lenovo'

import unittest

def setUpModule():
    print('***************Module Begin*************')

def tearDownModule():
    print('***************Module End****************')

class AnotherClass(unittest.TestCase):

    # def __init__(self):
    #     self.assertEqual(2,2)
    # def setUp(self):
    #     print('77777777777777777777')
    # def tearDown(self):
    #     # print('777777777777777777777')
    def test_add(self):
        print('I am the adding test')


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('&&&&&&&&&&&&& Class Begin &&&&&&&&&&&&')

    @classmethod
    def tearDownClass(cls):
        print('&&&&&&&&&&&&& Class End &&&&&&&&&&&&&')

    def setUp(self):
        print('test begin')

    def tearDown(self):
        print('test end')

    def test_case(self):
        print('test case 1')

    def test_case2(self):
        print('test case 2')

if __name__ == '__main__':
    unittest.main()



