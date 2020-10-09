# def fix_import(s):
#     a = ""
#     b = s.split()
#     for item in b[2:]:
#         a += item + " "
#     a += b[0]+" "+b[1]

#     return a


def fix_import(s):
    return f"from {s.split()[-1]} import {s.split()[1]}"


print(fix_import("import object from module_name"))
