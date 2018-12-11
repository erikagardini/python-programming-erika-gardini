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