input_file = open("hello.txt", "r")

print("First pass:")
for line in input_file.readlines():
    print(line, end="")

print("\n\n Second pass:")

for line in input_file.readlines():
    print(line, end="")


input_file.close()
