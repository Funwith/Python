# -*- coding: utf-8 -*-
__author__ = 'Vietworm'

'''
Tính S(n) = 1 + 2 + 3 + ... + n
Phân tích:
 - Xác định điều kiện dừng:  Nếu n == 1 thì return 1
 - Công thức: S(n) = S(n - 1) + n
'''

# Sử dụng phương pháp đệ quy


def S(n):
    if n == 1:
        return 1
    return S(n - 1) + n

# Không sử dụng đệ quy


def Si(n):
    tong = 0
    for i in range(n + 1):
        tong += i
    return tong


# Sử dụng đệ quy đuôi (Tail recursive)


def tail(n, x=1):
    if n == 1:
        return x
    return tail(n - 1, x + n)


print "Kết quả {}! = {}".format(4, S(4))
print "Kết quả {}! = {}".format(5, Si(5))
print "Kết quả {}! = {}".format(5, tail(5))
