# average_function.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a function that calculates the average of the values of
# any vector of 10 numbers 
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average 
# Define separate functions for the input and for calculating the average

'''
pseudo-code:
1)define a function with the command "def" called "avg" with only one parameter in input, called vector
    2)into the function "avg": define the variable "sum" and put it equal to 0
    3)define the variable "count" and put it equal to 0
    4)use a loop (ex. for) to obtain each element of the vector given in input
        5)into the loop: sum the current value to the variable accumulator "sum"
        6)increment the variable "count"
    7)in the end of the loop return the value given by "sum / count"
    NB: in python3 the results is automatically converted in float, in python the cast float() it is necessary

8)define a function with the command "def" called "set_vector" without parameter in input
    9)into the function "set_vector" create an empty list "vector" with []
    10)create a loop (ex. 10) for exactly 10 iteration (ex. range 0, 10)
        11)into the loop: use the command "input" to insert the number and store it into a variable
        12)use append to add the variable of step "11" into the vector,
            but first change the type of the variable in integer using int(variable)
    13) return the vector

14)Main program: call the function set_vector and save the result into a variable "vector"
15)call the function avg and gives as input the vector "vector"
16)store the result of the function avg into a variable called "mean"
14)print the vector "vector" and the variable "mean"
'''

def avg(vector):
    sum = 0
    count = 0
    for el in vector:
        sum = sum + el
        count = count + 1
    return sum / count


def set_vector():
    vector = []
    for i in range(0, 10):
        num = input("Insert a number: ")
        vector.append(int(num))
    return vector


#MAIN PROGRAM
vector = set_vector()
mean = avg(vector)
print("Vector: ", vector)
print("AVG: ", mean)