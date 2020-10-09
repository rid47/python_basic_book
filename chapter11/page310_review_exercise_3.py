source = open("hi.txt", "r")
dest = open("output.txt", "w")

for line in source.readlines():
    dest.writelines(line)

source.close()
dest.close()
