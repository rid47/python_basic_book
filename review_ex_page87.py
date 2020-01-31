def my_lowercse_function(myString):
    return myString.lower()

# def my_uppercase_function(myString):
#     return myString.upper()

value = my_lowercse_function("Animal")
value2 = my_lowercse_function("Honey Bee")
value3 = my_lowercse_function("Honeybadger")
print(f"{value}\n{value2}\n{value3}\n")

print(value.upper())
print(value2.upper())
print(value3.upper())

string = "    File Mignon"
print(string.lstrip())
string2 = "Brisket    "
print(string2.rstrip())
string3 = "Cheeseburger     "
print(string3.strip())

def result(string):
    return string.startswith("be")

string = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "bEautiful"

print(result("Becomes"))
