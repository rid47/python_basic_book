n = int(input("Enter a number:"))
sum = 0

while n > 0:
    reminder = n % 10
    sum += reminder
    n = n // 10

print(f"Sum of number: {sum}")
