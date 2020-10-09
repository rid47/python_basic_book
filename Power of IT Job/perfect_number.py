start_value = int(input("Enter start range: "))

end_value = int(input("Enter end range: "))

number = start_value
number_list_to_consider = []
while(number <= end_value):
    # print(number)
    number_list_to_consider.append(number)
    number += 1


print(number_list_to_consider)


def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


for number in number_list_to_consider:
    value = perfect_number(number)
    if value is True:
        print(f"{number} is perfect number")
