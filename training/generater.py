# -*- coding: utf-8 -*-
__author__ = 'Vietworm'


def dummy():
    print("You won't see me when created!")
    yield 1
    print("You didn't see me!")
    yield 2
    print("Good bye!")

gen = dummy()
gen.next()
gen.next()


myList = [x*x for x in range(3)]
for i in myList:
    print(i)