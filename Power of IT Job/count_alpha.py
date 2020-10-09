s = input("Enter your string:")

alphabets = 0
digits = 0
others = 0

for char in s:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    else:
        others += 1


print(f"Alpahbest: {alphabets}\ndigits:{digits}\nothers:{others}")
