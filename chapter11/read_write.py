with open("hello.txt", "r") as source, open("hi.txt", "w") as dest:
    for line in source.readlines():
        dest.write(line)

