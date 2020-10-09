def repeation(txt, n):
    return '' if not n else txt + repeation(txt, n-1)

print(repeation("hi",3))
