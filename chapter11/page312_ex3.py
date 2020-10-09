with open("hi.txt", "r") as source, open("output.txt", "w") as dest:
    for line in source.readlines():
        dest.writelines(line)
