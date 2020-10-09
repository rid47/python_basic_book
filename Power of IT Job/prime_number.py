start_value = int(input("Enter start range: "))

end_value = int(input("Enter end range: "))


def prime_number_check(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
            break

    if count == 0:
        return True
    else:
        return False


for number in range(start_value, end_value+1):
    value = prime_number_check(number)

    if value is True:
        print(f"{number} is prime")
    else:
        pass
