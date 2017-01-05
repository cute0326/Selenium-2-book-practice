# -*- coding: utf-8 -*-
__author__ = 'lenovo'

from xml.dom import minidom

dom = minidom.parse('info.xml')

root = dom._get_documentElement()

provinces = root.getElementsByTagName('province')
cities = dom.getElementsByTagName('city')

nets = root.getElementsByTagName('browser')
B1 = nets[0].firstChild.data
print(B1)

p2 = provinces[1].firstChild.data

print(p2)

c1 = cities[2].firstChild.data
print(c1)