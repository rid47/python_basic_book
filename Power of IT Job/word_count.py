n = input("Enter your string: ")

word_count = 0

for char in n:
    if char == " ":
        word_count += 1
# in order to consider the last word in string
word_count += 1
print(f"Your string has {word_count} words")
