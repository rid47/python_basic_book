n = input("Enter binary no to convert:")
n = n[::-1]

decimal = 0
for index, digit in enumerate(n):
    # print(f"power: {p}")
    # print(f"dec:{d}")
    decimal += int(digit) * pow(2, index)

print(f"Decimal: {decimal}")
