# -*- coding: utf-8 -*-
__author__ = 'lenovo'

import os

result_dir = './'

lists = os.listdir(result_dir)

lists.sort(key = lambda fn: os.path.getmtime(result_dir + '\\' + fn))

print('最新文件为:'+ lists[-1])

file = os.path.join(result_dir,lists[-1])
print(file)