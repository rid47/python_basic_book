# rain = input("Is it raining? (yes/no) ")
# umbrella = input("Do you have an umbrella? (yes/no) ")

# if rain == "yes" and umbrella == "yes":
#     print("Don't forget your umbrealla")
# elif rain == "yes" and umbrella == "no":
#     print("Take a rain coat or buy one")
# elif rain == "no" and umbrella == "yes":
#     print("Need not to take umbrella")
# else:
#     print("Have a good day")


def abs_val(num):
    if num < 0:
        return -num
    elif num == 0:
        return 0
    else:
        return num


result = abs_val(-4)
print(result)
result = abs_val(0)
print(result)
result = abs_val(78.3)
print(result)
