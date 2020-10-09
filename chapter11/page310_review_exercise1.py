file = open("hi.txt", 'r')
for line in file.readlines():
    print(line, end="")
file.close()
