import math

ATP = 3.5
ADP = 1.8
Pi = 5.0

DG0 = -30.5
R = 0.00831
T = 298

temp = ADP * Pi / ATP 
DG = DG0 + R*T* math.log(temp,2)

print("the Gibbs energy is ", DG)