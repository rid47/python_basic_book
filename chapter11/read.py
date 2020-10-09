input_file = open("hello.txt", "r")

line = input_file.readline()

while line != "":
    print(line, end="")
    line = input_file.readline()

input_file.close()
