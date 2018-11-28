file = open("file_prova.txt")

#print(file.read())

while 1:
    line = file.readline()
    if not line:
        break
    print(line)