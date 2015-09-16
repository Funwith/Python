# -*- coding: utf-8 -*-
__author__ = 'Vietworm'


#Read the lines from the file
R = open('test.db')
print R
for line in R.readlines():
    print(line, '')