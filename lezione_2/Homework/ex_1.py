import math

#1
num = 7
print(num)

#2
pi = 3.14

#4
avg = (num + pi) / 2

#5
dist_num = abs(num - avg)
dist_pi = abs(pi - avg)

#6
avg_dist = (dist_num + dist_pi) / 2

#7
new_num = float(num) - 1

#8
print(new_num)

pi = 3.14

avg = (new_num + pi) / 2

dist_num = abs(new_num - avg)
dist_pi = abs(pi - avg)

#9
x1 = 2
y1 = 4
x2 = 1
y2 = 6

euc_dist = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))
print(euc_dist)

#10
prob = 0.7
ic = - (math.log(prob, 2))
print(ic)
