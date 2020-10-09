data = ((1, 2), (3, 4))

i = 1
for t in data:
    print(f"Row {i} sum: {sum(t)}")
    i = i + 1


number = [4, 3, 2, 1]
number_copy = number[:]
number.sort()
print(f"number: {number}")
print(f"number_copy: {number_copy}")
print(f"number sorted in ASC order: {number}")
