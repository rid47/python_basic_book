def f(n):
    return 1 if not n else n * f(n-1)

print(f(4))
