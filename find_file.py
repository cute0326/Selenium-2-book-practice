# -*- coding: utf-8 -*-
__author__ = 'lenovo'

import os

result_dir = './'

lists = os.listdir(result_dir)

# print(os.path.getctime('runtest.py'))
lists.sort(key = lambda fn: os.path.getctime(result_dir + '\\' + fn))

print('最新文件为:'+ lists[-1])


print(lists[-1])