with open("hi.txt", 'r') as file:

    for line in file.readlines():
        print(line, end="")
