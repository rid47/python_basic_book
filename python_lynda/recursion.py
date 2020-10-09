n = input("Enter a positive integer whose factorial you want to calculate:")
n = int(n)
def factorial(n):
    """ Return the factorial of positive integer n. """
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


result = factorial(n)
print(f"Factorial of {n} is {result}")
