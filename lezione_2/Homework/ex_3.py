def increase(n):
	return n + 1

def add(a, b):
	return a + b

def add3(a, b, c):
	return a + b + c

def add5(a, b, c, d, e):
	return a + b + c + d + e

def concatManyTimes(n, s):
	s_new = ''
	for i in range(0, n):
		s_new = s_new + s
	return s_new

def concatManyTimesWithComma(n, s):
	s_new = ''
	for i in range(0, n):
		s_new = s_new + s
		if(i < n - 1):
			s_new = s_new + ","
		
	return s_new

def concatManyTimesWithSep(n, s, sep):
	s_new = ''
	for i in range(0, n):
		s_new = s_new + s
		if(i < n - 1):
			s_new = s_new + sep

	return s_new

a = 5
b = 6
c = 2
d = 3
e = 1

print(increase(a))
print(add(a,b))
print(add3(a,b,c))
print(add5(a,b,c,d,e))
print(concatManyTimes(3, 'dad'))
print(concatManyTimesWithComma(3, 'dad'))
print(concatManyTimesWithSep(3, 'dad', '*'))