__author__ = 'Vietworm'

a, b = 0, 1

if a < b:
    print('a = {} is less than b({})'.format(a, b))
else:
    print('a = {} is greater than b({})'.format(a, b))

print("Foo" if a < b else "Bar")


#Read the lines from the file
R = open('fibonacci.py')
for line in R.readlines():
    print(line, '')