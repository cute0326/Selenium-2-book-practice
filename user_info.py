# -*- coding: utf-8 -*-
__author__ = 'lenovo'

import csv

data = csv.reader(open('info.csv','r'))

for user in data:
    print(user[2])