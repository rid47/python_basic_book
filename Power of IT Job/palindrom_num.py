n = int(input("Enter a number:"))

tmp = n
rev = 0

while tmp > 0:
    digit = tmp % 10
    rev = rev * 10 + digit
    tmp = tmp//10

if rev == n:
    print("The number is palindrom")
else:
    print("The number is not palindrom")
