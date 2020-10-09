def addFive(x):
    print(x + 5)


addFive(30)
addFive(62.5)


def greeting():
    print("Hi there!")


greeting()


def greet(name):
    print("Hi " + name)


greet("Max")


def square(x):
    return x * x


result = square(5)

anotherOne = square(result)

print(result)
print(anotherOne)


def sumOfSquares(x, y):
    square1 = x * x
    square2 = y * y
    return square1 + square2


result = sumOfSquares(2, 3)
print(result)


def is_it_raining():
    raining = input("Is it raining today?")
    return raining


monday_rain = is_it_raining()
print(monday_rain)
