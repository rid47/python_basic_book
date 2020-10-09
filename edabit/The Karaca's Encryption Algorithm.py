d = {
    "a": 0,
    "e": 1,
    "i": 2,
    "o": 2,
    "u": 3,
}


def encrypt(word):
    rev_word = word[::-1]
    enc_word = ""
    for char in rev_word:
        if char in d:
            enc_word += str(d[char])
        else:
            enc_word += char

    return enc_word+"aca"


print(encrypt("karaca"))
