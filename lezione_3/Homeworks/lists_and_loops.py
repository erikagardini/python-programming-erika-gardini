import math

def product(a, l):
	new_l = []
	for el in l:
		new_l.append(el * a)
	return new_l

def bernsteinPolynomial(n, beta, x):
	sum = 0
	for i in range (0, n):
		sum = sum + (beta[i] * x)

def frequencyDNA(dna):
	num_a = 0
	num_c = 0
	num_g = 0
	num_t = 0

	for el in dna:
		if el == 'A':
			num_a = num_a + 1
		elif el == 'C':
			num_c = num_c + 1
		elif el == 'G':
			num_g = num_g + 1
		else:
			num_t = num_t + 1

	return num_a, num_c, num_g, num_t 

def frequency(list):
	elements = []
	freq = []
	trovato = 0

	for el in list:
		for i in range(0, len(elements)):
			if el == elements[i] and trovato == 0:
				trovato = 1
				freq[i] = freq[i] + 1
		if trovato == 0:
			elements.append(el)
			freq.append(1)
		trovato = 0
	return elements, freq

def find_max(l):
	max = l[0]
	index_max = 0
	for i in range(0, len(l)):
		if l[i] > max:
			max = l[i]
			index_max = i

	return index_max

def avg(vect):
	sum = 0
	count = 0
	for el in vect:
		sum = sum  + el
		count = count + 1

	return float(sum) / count

def factorial(number):
	fact = 1
	for i in range(1, (number+1)):
		fact = fact * i
	return fact

def factorial_rec(acc, number):
	if number == 1:
		return acc
	else:
		return factorial_rec(acc * number, number-1)

def median(vec):
	len_v = len(vec)
	print(len_v)
	if len_v % 2 == 0:
		index_1 = int(len_v / 2)
		print(index_1)
		index_2 = int((len_v / 2) - 1)
		print(index_2)
		return (vec[index_1] + vec[index_2]) / 2
	else:
		index = int(len_v / 2)
		return vec[index]

def variance(l):
	mean = avg(l)
	n = len(l)
	first_part = 1 / (n - 1)
	somma = 0
	for el in l:
		somma = somma + math.pow((el - mean), 2)

	return first_part * somma

def std(l):
	return math.sqrt(variance(l))

def z_score(l):
	z = []
	for el in l:
		z.append( (el - avg(l)) / std(l) )
	return z

def sum_of_two_vector(v1, v2):
	c = []
	for i in range(0, len(v1)):
		c.append(v1[i] + v2[i])
	return c

def dotProduct(v1, v2):
	somma = 0
	for i in range(0, len(v1)):
		somma = somma + (v1[i] * v2[i])

	return somma

def root_mean_square(p1, p2):
	somma = 0
	for i in range(0, len(p1)):
		somma = somma + math.pow(math.abs(p1[i] - p2[i]), 2)
	somma = somma / len(p1)
	return math.sqrt(somma)

def find_p(el, p):
	for i in range(0, len(p)):
		if p[i][0] == el:
			return p[i][1]

def entropy(s, p):
	somma = 0
	for el in s:
		prob = find_p(el, p)
		somma = somma + (prob * math.log(prob))
	return (-somma)

def cov(v1, v2):
	somma_1 = 0
	somma_2 = 0
	somma_3 = 0

	for el in v1:
		somma_1 = somma_1 + (el)
	for el in v2:
		somma_2 = somma_2 + (el)
	for i in range(0, len(v1)):
		somma_3 = somma_3 + (v1[i] * v2[i])

	return ( ((1 / len(v1)) * somma_3 ) - (somma_1 * somma_2) )

def t_value(a, b):
	mean_a = avg(a)
	mean_b = avg(b)
	std_a = std(a)
	std_b = std(b)
	n_a = len(a)
	n_b = len(b)

	temp = (std_a / math.sqrt(n_a)) + (std_a / math.sqrt(n_b))
	t = (mean_a - mean_b) * math.pow((temp), -1)

	return t

def chi_square(o, e)
	somma = 0
	for i in range(0, len(o)):
		somma = somma + ( math.pow((o[i] - e[i]), 2) / e[i] )

	return somma


dna = 'AACTGTCGATCGATCGCTGT'
num_a, num_c, num_g, num_t = frequencyDNA(dna)
print(num_a, num_c, num_g, num_t)

l = [1, 2, 3, 4, 5, 1, 1, 3, 6, 2, 9]
elements, freq = frequency(l)
print(elements)
print(freq)

index_max = find_max(freq)
print(elements[index_max], freq[index_max])

l = ['a', 'g', 'g', 'g', 'e', 'h', 'a', 'd', 'f', 'x', 'c']
elements, freq = frequency(l)
print(elements)
print(freq)

index_max = find_max(freq)
print(elements[index_max], freq[index_max])

vect = [3, 4, 7, 1, 2, 3, 5]
print(avg(vect))

print(factorial(4))
print(factorial(3))
print(factorial(5))
print(factorial_rec(1, 4))
print(factorial_rec(1, 5))

print(median(vect))
print(variance(vect))
print(std(vect))

p = [['a', 0.1], ['b', 0.5], ['c', 0.2], ['d', 0.2]]
s = 'aaaabbcd'
print(entropy(s, p))
