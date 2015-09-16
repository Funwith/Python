# -*- coding: utf-8 -*-
__author__ = 'Vietworm'


def test(how, who, why, what, *args):
    print (how,who,why,what, args, type(args))
    for i in args:
        print i,

#test(05, 11, 1994, 254, 56, 84, 214)


def test2(how, who, why, *args, **kwargs):
    print(how, who, why, args, kwargs)
    for k in kwargs:
        print('{}'.format(kwargs[k])),

test2(05, 11, 1994, 254, 56, 84, 214, one=1, two=2)

