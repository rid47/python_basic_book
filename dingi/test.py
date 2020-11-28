def enc_password(password):
    password_list = []
    password_list[:0] = password
    # print(password_list)

    for index, char in enumerate(password_list):
        # print(index, char)
        if char.isdigit():
            password_list[index] = "@"
            password_list.insert(0, char)

    # print(password_list)

    for index, char in enumerate(password_list):
        if char.islower():
            if password_list[index+1].isupper():
                # print(f"append ! & # on index {index+2, index+3}")
                password_list.insert(index+2, "!")
                password_list.insert(index+3, "#")

    # print(password_list)

    enc_password = ""
    for char in password_list:
        enc_password += char
    return enc_password


def decrypt_password(password):
    password_list = []
    password_list[:0] = password

    for index, char in enumerate(password_list):
        if char.islower():
            if password_list[index+1].isupper():
                # print(f"remove ! & # from index {index+2, index+3}")
                del password_list[index+2:index+4]
                # del password_list[index+3]

    # print(f"decrypted password: {password_list}")

    digit_index = []
    for index, char in enumerate(password_list):

        if char.isdigit():
            # password_list.pop(index)
            # print(char)
            # print(index)
            digit_index.append(index)

    # print(digit_index)
    for index in digit_index:
        try:

            password_list[password_list.index("@")] = password_list[index]
            password_list[index] = None
        except:
            pass
    # print(f"decrypted password2: {password_list}")

    decrypted_pass = ""

    for data in password_list:
        if data is not None:
            decrypted_pass += data

    # print(decrypted_pass)
    return decrypted_pass


password = input("Enter your password:")
print(f"Given password: {password}")
encrypted_password = enc_password(password)
print(f"Encrypted Password: {encrypted_password}")
decrypted_password = decrypt_password(encrypted_password)
print(f"Decrypted Password: {decrypted_password}")

# decrypt_password("32HelO!#Dingi@@")
