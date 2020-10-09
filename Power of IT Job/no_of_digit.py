n = int(input("Enter a number:"))

no_of_digit = 0


while(n != 0):
    last_digit = n % 10
    no_of_digit += 1
    n = n//10

print(f"No of digits: {no_of_digit}")
