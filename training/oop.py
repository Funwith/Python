# -*- coding: utf-8 -*-
__author__ = 'Vietworm'

# Class constructor


class Fibonacci():
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def series(self):
        while True:
            yield self._b
            self._a, self._b = self._b, self._a + self._b


f = Fibonacci(0, 1)
for r in f.series():
    if r > 100:
        break
    print r,


