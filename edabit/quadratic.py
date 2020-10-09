import math


def quadratic_equation(a, b, c):
    # value = math.sqrt(b*b - (4*a*c))
    # return (-b+value)/(2*a)
    return (-b+math.sqrt(b*b -(4*a*c)))/(2*a)


r = quadratic_equation(1, -12, -28)
print(r)
