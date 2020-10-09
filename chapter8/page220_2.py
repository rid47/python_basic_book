given_string = input("Enter a string: ")

try:
    n = int(input("Enter an integer: "))
    char = given_string[n]
    print(f"character at index {n} is {char}")
except ValueError:
    print("Invalid integer!")

except IndexError:
    print("Invalid index!")
