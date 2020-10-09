def lcm(a, b):
    if a > b:
        max = a
    else:
        max = b
    while True:
        if max % a == 0 and max % b == 0:
            lcm = max
            break
        else:
            max += 1
    return lcm


a = int(input("Enter a nubmer:"))
b = int(input("Enter another nubmer:"))

print(f"LCM of {a} and {b} is {lcm(a,b)}")
