__author__ = 'lenovo'

import sys
sys.path.append('../..')
from calculator import Count
import unittest

class TestSub(unittest.TestCase):
    'testsub.py'
    def setUp(self):
        # print('testsub.py')
        pass
    def tearDown(self):
        # print('test case end')
        pass
    def test_sub(self):
        j = Count(2,3)
        self.assertEqual(j.sub(),-1)

    def test_sub2(self):
        j = Count(71,46)
        self.assertEqual(j.sub(),25)

if __name__ == '__main__':
    unittest.main()