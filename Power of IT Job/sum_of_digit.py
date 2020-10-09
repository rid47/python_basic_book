n = int(input("Enter a number:"))

# pop out the last digit

sum = 0

while n > 0:
    last_digit = n % 10
    # print(last_digit)
    sum += last_digit
    n = n//10


print(sum)
