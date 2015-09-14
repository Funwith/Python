# -*- coding: utf-8 -*-

import math

"""
Tìm số fibonacci thứ n
"""
def fibo(n):
	if (n == 0 or n == 1):
		return 1
	else:
		return fibo(n - 1) + fibo(n - 2)
		
print fibo(6)


"""
Dãy số fibonacci nhỏ hơn 100
"""

def fibo2():
	a, b = 0, 1
	while b < 100:
		print b,
		a, b = b, a + b
		
fibo2()


def soNguyenTo(n):
	for x in range(2, int(math.ceil(math.sqrt(n)))):
		if (n%x == 0):
			return False
		else:
			return True
			
print '\n\n'  + str(soNguyenTo(73))		
	