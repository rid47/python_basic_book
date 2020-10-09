n = int(input("Enter no. of elements:"))

num_list = []
for i in range(1, n):
    num = int(input())
    num_list.append(num)

print(num_list)


even_num_list = []
for num in num_list:
    if num % 2 == 0:
        even_num_list.append(num)

print(f"Even numbers: {even_num_list}")
