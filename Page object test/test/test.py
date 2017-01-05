# coding:utf-8
__author__ = 'lenovo'

import sys
sys.path.append('./function')

from function import new_count

if __name__ == '__main__':
    test = new_count.B()
    print('in test.py')
    print(test.sub(5,2))