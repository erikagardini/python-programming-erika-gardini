import math

def distance_between_two_points(p1, p2):
	distance = math.sqrt( math.pow((p2[0] - p1[0]), 2) + math.pow((p2[1] - p1[1]), 2))

	return distance

#main
p1 = [2, 3]
p2 = [4, 1]
res = distance_between_two_points(p1, p2)
print(res)