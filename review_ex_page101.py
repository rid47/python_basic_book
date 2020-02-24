print("AAA".find('a'))

given_string = "Somebody said something to Samantha."
modified_string = given_string.replace("s", "x")
print(modified_string)

user_input = input("Enter a string")
search_result = user_input.find("a")
if search_result != -1:
    print("You have 'a' in your string")
else:
    print("You don't have 'a' in your string")
