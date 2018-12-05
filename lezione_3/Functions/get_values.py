def get_values(arg1, arg2):
	sum = arg1 + arg2
	difference = arg1 - arg2
	product = arg1 * arg2
	return sum, difference, product

[sum, difference, product] = get_values(5,4)
print(sum)
print(difference)
print(product)