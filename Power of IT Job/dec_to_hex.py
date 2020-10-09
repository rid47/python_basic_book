n = int(input("Enter decimal number to be converted to hex:"))

remainder = []
while n > 0:
    r = n % 16
    if r == 10:
        remainder.append("A")
    if r == 11:
        remainder.append("B")
    if r == 12:
        remainder.append("C")
    if r == 13:
        remainder.append("D")
    if r == 14:
        remainder.append("E")
    if r == 15:
        remainder.append("F")
    else:
        remainder.append(r)
    n = n // 16

# print(remainder[::-1])
number = ""
for i in remainder[::-1]:
    number += str(i)

print(number)
