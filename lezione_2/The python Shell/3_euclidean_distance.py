import math

a_x = 43.64
a_y = 30.72
a_z = 88.95
b_x = 45.83
b_y = 31.11
b_z = 92.04

d = ((b_x ** 2) - (a_x **2)) + ((b_y ** 2) - (a_y **2)) + ((b_z ** 2) - (a_z **2))

d = math.sqrt(d)

print("the distance is ", d)