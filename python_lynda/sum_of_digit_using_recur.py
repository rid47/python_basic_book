def sum_of_digit(n):
    if n < 10:
        return n
    else:
        all_but_last = n//10
        last = n % 10
        return sum_of_digit(all_but_last) + last


n = int(input("Enter a number: "))
result = sum_of_digit(n)
print(f"Sum of digits for number {n} is = {result}")
