# -*- coding: utf-8 -*-

"""
Tìm số fibonacci thứ n
"""
def fibo(n):
	if (n == 0 or n == 1):
		return 1
	else:
		return fibo(n - 1) + fibo(n - 2)
		
x = fibo(6)

print x

"""
Dãy số fibonacci nhỏ hơn 100
"""

def fibo2():
	a, b = 0, 1
	while b < 100:
		print b,
		a, b = b, a + b
		
fibo2()