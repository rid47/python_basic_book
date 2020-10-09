decimal_no = int(input("Enter a number: "))

bin_digit_list = []
while decimal_no != 0:
    bin_digit = decimal_no % 2
    bin_digit_list.append(bin_digit)
    decimal_no = decimal_no // 2


print(f"bin digit list: {bin_digit_list}")

bin_digit_list.reverse()

bin_number = ""
for i in bin_digit_list:
    bin_number += str(i)

print(f"converted bin no: {bin_number}")
