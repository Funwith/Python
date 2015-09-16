# -*- coding: utf-8 -*-

import math

#Tìm số fibonacci thứ n
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


#Dãy số fibonacci nhỏ hơn n
def fibo2(n):
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a + b


# Xác định số nguyên tố
def soNguyenTo(n):
    if n == 1:
        print("1 is special")
        return False
    for x in range(2, int(math.ceil(math.sqrt(n)))):
        if n % x == 0:
            return False
        else:
            return True