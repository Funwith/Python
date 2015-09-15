# -*- coding: utf-8 -*-
__author__ = 'Vietworm'

'''
Tính S(n) = 1 + 2 + 3 + ... + n
Phân tích:
 - Xác định điều kiện dừng:  Nếu n == 1 thì return 1
 - Công thức: S(n) = S(n - 1) + n
'''
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


print "Ket qua de quy cua {} la: {}".format(4,S(4))
print "Ket qua de quy cua {} la: {}".format(5,Si(5))