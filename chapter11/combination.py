def combinations(*items):
    result = 1
    for item in items:
        # print(item)
        if item == 0:
            continue
        result *= item
    return result


# print(combinations(2, 3))
# print(combinations(3, 7, 4))
# print(combinations(2, 3, 4, 5))
print(combinations(6, 7, 0))
