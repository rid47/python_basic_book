n = input("Choose an integer between -10 and 10 and enter it here: ")
n = int(n)
if n < 5:
    print("The integer you choose is less than 5")
else:
    print("The integer you choos is greater than 5")


def max(x, y):
    if x > y:
        return x
    else:
        return y


result = max(5, 7)
print(result)

result = max(-5, -7)
print(result)

result = max(10, 10)
print(result)
