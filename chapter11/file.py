output_file = open("hello.txt", "r")

# lines_to_write = [

#     "This is my file.",
#     "\nThere are many like it,",
#     "\nbut this one is mine.",
# ]

# output_file.writelines("\nNon SEQUITUR")

# print(output_file.readlines())

for line in output_file.readlines():
    print(line, end="")
output_file.close()
