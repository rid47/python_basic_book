thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
    print(x)

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)


a = {"1", "2", 3}
b = {4, 5, 6}

c = a.union(b)
print(c)


fruit = ("apple", "banana", "cherry")

fruit_set = set(fruit)
print(fruit_set)
