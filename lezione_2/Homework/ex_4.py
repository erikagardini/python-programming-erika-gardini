def sum_el(l1, l2, l3):
	l4 = []
	for i in range(0, len(l1)):
		l4.append(l1[i]+l2[i]+l3[i])
	return l4

l1 = [4,8,-9,'the']
l2 = ['silent force', 4.67,9]
l3 = l1 + l2
print(l3)

l1 = [2,3,4]
for el in l1:
	print(el + 3)
print(l2)

s = '23|64|354|-123'
l1 = []
num = ''
for el in s:
	if el.isdigit():
		num = num + el
		print(num)
	elif el == '-':
		if(num == ''):
			num = num + el
			print(num)
	else:
		if num.isdigit() or num[1:].isdigit():
			l1.append(float(num))
			num = ''
		else:
			num = ''

if num.isdigit() or num[1:].isdigit():
	l1.append(float(num))
	num = ''
print(l1)

s = "-1-987-6823-8261"
l2 = []
num = ''
for el in s:
	if el.isdigit():
		num = num + el
		print(num)
	else:
		if num.isdigit():
			l2.append(float(num))
			num = ''
		else:
			num = ''

if num.isdigit():
	l2.append(float(num))
	num = ''
print(l2)

l3 = [3.14,6.333,98.12,23.1]
s = ''
for el in l3:
	s = s + str(el)
	s = s + ','
print(s)

print(sum_el(l1,l2,l3))


		