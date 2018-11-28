from math import pi

#d = 10.0
#d = input("Insert the diameter:")
in_file = open('input_diameter.txt')
d = in_file.read()
d = float(d)

r = d / 2.0

V = (4.0/3.0)*pi*(r**3)
print(V)
