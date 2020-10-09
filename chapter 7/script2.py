def add_underscore(word):
    new_word = "_"
    for i in range(0, len(word)):
        new_word = new_word + word[i] + "_"
       
    return new_word

phrase = "hello"
print(add_underscore(phrase))
