__author__ = 'lenovo'

import sys
sys.path.append('../..')
from calculator import Count

import unittest

class TestAdd(unittest.TestCase):
    "testadd.py"
    def setUp(self):
        # print('testadd.py')
        pass


    def tearDown(self):
        # print('test case end')
        pass
    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)

    def test_add2(self):
        j = Count(41,76)
        self.assertEqual(j.add(),117)

if __name__ == '__main__':
    unittest.main()