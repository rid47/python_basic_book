given_string = input("Enter a number: ")
given_string_len = len(given_string)
slicedString = given_string[given_string_len::-1]
print(slicedString)

if given_string == slicedString:
    print("Palindrome")
else:
    print("Not Palindrome")
