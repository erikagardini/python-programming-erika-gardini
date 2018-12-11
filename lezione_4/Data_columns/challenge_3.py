def avg(list):
	count = 0
	sum = 0
	for el in list:
		count = count + 1
		sum = sum + el
	return sum / count


primary_len = []
secondary_len = []
with open("neuron_data_2.txt") as f:
	for line in f:
		res = line.split(" ")
		info = float(res[0])
		if info == 1:
			primary_len.append(float(res[-1]))
		elif info == 2:
			secondary_len.append(float(res[-1]))

print(primary_len)
print(secondary_len)

mean_primary = avg(primary_len)
mean_secondary = avg(secondary_len)
if mean_primary > mean_secondary:
	print("The mean_primary is on average longer")
else:
	print("The mean_secondary is on average longer")