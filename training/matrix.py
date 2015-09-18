fin = open('matrix.txt','r')
matrix = []
for i in range(5):
	arow = map(int, fin.readline().split(','))
	matrix.append(arow)
	
for i in matrix:
	print i
