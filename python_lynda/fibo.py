def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-1) + fibo(n-2))


n = int(input("Enter a positive number: "))

if n < 0:
    print("You entered a neg number")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        # print(i)
        print(fibo(i))
