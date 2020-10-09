def convert_cel_to_far(x):
    f = x * 9/5 + 32
    return round(f, 2)


def convert_far_to_cel(y):
    d = (y-32) * 5/9
    return round(d, 2)


temp_in_f = input("Enter a temperature in degrees F: ")
print(f"{temp_in_f} degrees F = {convert_far_to_cel(float(temp_in_f)): .2f} degrees C")

temp_in_d = input("Enter a temperature in degrees C: ")
print(f"{temp_in_d} degrees C = {convert_cel_to_far(float(temp_in_d)): .2f} degrees F")
