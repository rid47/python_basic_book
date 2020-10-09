number = input("Enter number: ")

reversed_number = ""
number_lenght = len(number)
# print(number_lenght)

for i in range(number_lenght-1, -1, -1):
    reversed_number += str(number[i])

# print(number)
# print(reversed_number)

if number == reversed_number:
    print("palindrome")
else:
    print("Non palindrome")
