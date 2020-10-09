def computeGCD(x,y):
    if x > y:
        small = y
    else:
        small = x

    for i in range(1, small+1):
        if x % i == 0 and y % i == 0:
            gcd = i

    return gcd


a = int(input("Enter a number:"))
b = int(input("Enter second number:"))
gcd = computeGCD(a,b)


# a * b = gcd(a,b) * lcm(a,b)

lcm = (a*b)/gcd


print(f"GCD of {a} and {b} is {gcd}")

print(f"LCM of {a} and {b} is {lcm}")
