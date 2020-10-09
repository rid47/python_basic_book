a = [1, 2, 3, 4, 5]

b = [x * 5 for x in a]

print(b)

c = (x * 5 for x in a)

print(c)

next(c)

next(c)

print(next(c))
