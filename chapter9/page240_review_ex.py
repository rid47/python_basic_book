cardinal_numbers = ("first", "second", "third")
print(cardinal_numbers)
print(cardinal_numbers[1])
position1, position2, position3 = cardinal_numbers

print(position1)
print(position2)
print(position3)

my_name = tuple("Ridwan")
print(type(my_name))
if "x" in my_name:
    print("Yes")
else:
    print("No")


changed_name = tuple(my_name[1:])

print(changed_name)
