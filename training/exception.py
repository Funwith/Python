# -*- coding: utf-8 -*-
__author__ = 'Vietworm'

try:
    f = open('conditionals1.py')
    for i in f.readlines():
        print i
except IOError as e:
    print "Script has exception on running processed!\nError: {}".format(e)
    raise ValueError('Test raise')
