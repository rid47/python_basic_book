while True:
    try:
        n = int(input("Enter an integer: "))
        print(f"You entered: {n}")
        break
    except ValueError:
        print("try again")
