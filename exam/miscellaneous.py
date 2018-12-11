# miscellaneous.py
# For the following exercises, pseudo-code is not required

# Exercise 1
# Create a list L of numbers from 21 to 39
# print the numbers of the list that are even
# print the numbers of the list that are multiples of 3
print("###Ex. 1")
l = []
for i in range(21, 40):
    l.append(i)
print("List:", l)

print("Even elements")
for el in l:
    if el % 2 == 0:
        print(el)

print("Multiples of 3")
for el in l:
    if el % 3 == 0:
        print(el)

# Exercise 2
# Print the last two elements of L
print("###Ex. 2")
print("The last two elements of L: ", l[-2:])

# Exercise 3
# What's wrong with the following piece of code? Fix it and
# modify the code in order to have it work AND to have "<i> is in the list"
# printed at least once

'''
L = ['1', '2', '3']
for i in range(10)
    if i in L:
    print(i is in the list)
    else:
    print(i not found)  
'''
print("###Ex. 3")
L = ['1', '2', '3']
for i in range(2, 10):
    if str(i) in L:
        print(i, "is in the list")
    else:
        print(i, "not found")

# Exercise 4
# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list
print("###Ex. 4")
f = open("sprot_prot.fasta")
line = f.readline()
print("Line: ")
print(line)

res = line.split('OS=')
print("The second element after the split is: ")
print(res[1])

# Exercise 5
# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string
print("###Ex. 5")
res_1 = res[1].split(' ')
print("The results of the split with blanks as separators is: ", res_1)

s = res_1[0] + " " + res_1[1]
print("The results after concat is: ", s)

# Exercise 6
# reverse the string 'asor rosa'
print("###Ex. 6")
s = 'asor rosa'
print("Reverse string: ", s[::-1])

# Exercise 7
# Sort the following list: L = [1, 7, 3, 9]
print("###Ex. 7")
l = [1, 7, 3, 9]
print("List: ", l)
l.sort()
print("Sorted list: ", l)

# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L
print("###Ex. 8")
l = [1, 7, 3, 9]
l_1 = l.copy()
l_1.sort()
print("List: ", l)
print("Sorted list: ", l_1)

# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6
table = [[2,4], [3,6]]
f = open("save_table.txt", "w")
for el in table:
    s = ""
    for i in range(0, len(el)):
        s = s + str(el[i])
        if i != len(el)-1:
            s = s + ","
        else:
            s = s + "\n"
    f.write(s)


