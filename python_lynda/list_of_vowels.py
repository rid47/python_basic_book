vowels = ['a', 'e', 'i', 'o', 'u']
vowels_in_word = []

for char in 'serendiptous':
    # print(char)
    if char in vowels and char not in vowels_in_word:
        vowels_in_word.append(char)

print(vowels_in_word)
