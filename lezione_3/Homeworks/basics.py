import math

def roots(a, b, c):
	delta = math.sqrt(math.pow(b,2) - (4*a*c))
	if delta > 0:
		x1 = (- b + delta) / (2*a)
		x2 = (- b - delta) / (2*a)
		return x1, x2
	else
		return -1, -1

def product(a, p):
	p[0] = p[0] * a
	p[1] = p[1] * a
	return p

def distance(p1, p2):
	return math.sqrt(math.pow((p2[0]-p1[0]),2) + math.pow((p2[1]-p1[1]),2) + math.pow((p2[2]-p1[2]),2))

def bernsteinBasis(i, n, t):
	binCoef = fact(n) / (fact(n-i) - fact(i))
	return binCoef * math.pow((1-t), (n-i)) * math.pow(t, i)

#1 if true, 0 otherwise
def isEven(n):
	if n % 2 == 0:
		return 1
	else:
		return 0
  

