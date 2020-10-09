def factorial(n):
    value = 1
    for i in range(n, 1, -1):
        value *= i
    return value


n = int(input("Enter n for finding nCr:"))
r = int(input("Enter r for finding nCr:"))


if r > 0 and n > r:
    result = factorial(n)/(factorial(r)*factorial(n-r))
    print(result)
else:
    print("Invalid input!")
