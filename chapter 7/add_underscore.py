def add_underscores(word):
    modified_word = ""
    for char in word:
        modified_word += "_"+char

    return modified_word+"_"


word = add_underscores("python")
print(word)
