
lenght = []
with open("neuron_data.txt") as f:
	for line in f:
		res = line.split(" ")
		lenght.append(float(res[-1]))

print(lenght)