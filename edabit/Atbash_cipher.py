original_str_cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_str_cap = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
original_str_sml = "abcdefghijklmnopqrstuvwxyz"
cipher_str_sml = "zyxwvutsrqponmlkjihgfedcba"


def atbash(txt):
    cipher_txt = ""
    for char in txt:
        if char.isalpha():
            if char.isupper():
                cipher_txt += cipher_str_cap[original_str_cap.find(char)]
            else:
                cipher_txt += cipher_str_sml[original_str_sml.find(char)]
        else:
            cipher_txt += char

    return cipher_txt


txt = atbash("abcdefghijklmnopqrstuvwxyz")
print(txt)
