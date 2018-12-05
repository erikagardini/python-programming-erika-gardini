import math

def radici(a, b, c):
	temp = math.pow(b, 2) - (4 * a * c)
	x1 = (b + math.sqrt(temp)) / (2 * a)
	x2 = (b - math.sqrt(temp)) / (2 * a)
	return x1, x2


a = 2
b = 8
c = 2

[x1, x2] = radici(a, b, c)
print(x1)
print(x2)