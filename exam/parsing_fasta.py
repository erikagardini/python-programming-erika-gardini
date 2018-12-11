# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght 
# Use separate functions for the input and the output 

'''
Pseudo-code:
1)define a function called "gives_lines_of_a_file_as_list" with only one parameter in input: "filename"
    2)into the function: define an empty list called "lines"
    3)open the file called "filename"
    4)create a loop in order to read each lines of the file
        5)into the loop: append each line at the list "lines"
    6)in the end of the loop, return the list "lines"

7)define a function called "write_lines_into_a_file" with only one parameter in input: "lines"
    8)into the function: open a file in "w" mode (you can choose the name of the file)
    9)use the command "writelines" to write all the content of the list "lines" given in input

10)define a function called "get_OS" with only one parameter in input "line"
    11)into the function: split the line with sep "OS=" and save the result
    12)from the previuos result takes the second element and save it
    13)split the result of the step "12" with sep " "
    14)concat the first and the second elements of the step "13"
    15)return the result of the step "14

16)define a function called "lenght" with only one parameter in input "seq"
    17)into the function: define and accumulator "count" and put it equal to 0
    18)use a loop to analyse each element of the list "seq"
        19)into the loop: sum the lenght of the element of the list "seq" to the acc "count"
    20)return the variable "count"

21)the main program: use the function "gives_lines_of_a_file_as_list" to obtain all the lines of the file into a list
22)use a loop to analyse each line of the list "lines"
    23)into the loop: find each line that containes ">" and that doesn't contains "Homo sapiens"
    24)save this line and the n following lines, until the next ">"
    25)repeat this process in order to analyse each lines into the list "lines"
26)store the saved information permanently using the function "write_lines_into_a_file"
'''

#This function reads from file and return a list as results
def gives_lines_of_a_file_as_list(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line)
    return lines

#This function writes the list into the files
def write_lines_into_a_file(lines):
    f = open("notHomoSapiens.fasta", "w")
    f.writelines(lines)

def get_OS(line):
    res = line.split('OS=')
    res_1 = res[1].split(' ')
    s = res_1[0] + " " + res_1[1]
    return s

def get_lenght(seq):
    count = 0
    for el in seq:
        count = count + (len(el) - 1) #the character \n is not considered
    return count

#MAIN PROGRAM

#Read from file fasta
lines = gives_lines_of_a_file_as_list("sprot_prot.fasta")

to_store = []

for i in range(0, len(lines)):
    #Check if the line contains ">" and if doesn't contains "Homo sapiens"
    if lines[i].find(">") != -1 and lines[i].find("Homo sapiens") == -1:
        print("###")
        #Store the header
        to_store.append(lines[i])
        #Get the source_organism
        source_organism = get_OS(lines[i])
        #Analyse the sequence
        seq = []
        i = i + 1
        #Store all until the next ">"
        while lines[i].find(">") == -1:
            to_store.append(lines[i])
            seq.append(lines[i])
            i = i + 1
        #Get the sequence len
        lenght = get_lenght(seq)

        #Print!!!
        print("The source organism is: ", source_organism, "and the lenght of the sequence is ", lenght)

#Store the selected lines into the file output
write_lines_into_a_file(to_store)

