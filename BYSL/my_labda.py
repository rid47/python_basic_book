def squareof(x):
    return x*x


print(squareof(5))


f = lambda x: x*x
print(f(5))


numbers = [75, 85, 14, 23, 56, 31, 44]

remainder = map(lambda num: num%5, numbers)

for i in remainder:
    print(i)

print(type(remainder))
