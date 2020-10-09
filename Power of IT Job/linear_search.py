x = input("Enter a string:")
y = input("Enter a char to search:")


counter = 0
for char in x:
    if char == y:
        counter += 1


if counter > 0:
    print(f"{y} char found in {x}")
else:
    print(f"{y} not found!")
