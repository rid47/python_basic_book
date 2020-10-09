a_string = "cba"

sorted_char = sorted(a_string)  # about sorted: https://www.w3schools.com/python/ref_func_sorted.asp#:~:text=The%20sorted()%20function%20returns,string%20values%20AND%20numeric%20values.
print(sorted_char)

a_string = "".join(sorted_char)  # about join: https://www.w3schools.com/python/ref_string_join.asp
print(a_string)
