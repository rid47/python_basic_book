def invest(amount, rate, years):
    for year in range(1, years+1):
        amount = round(amount*(1+rate), 2)
        print(f"year {year}: {amount}")


invest(100, 0.05, 4)
