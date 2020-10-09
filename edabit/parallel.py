def lines_are_parallel(l1, l2):
    s1 = l1[0]/l1[1]
    s2 = l2[0]/l2[1]
    if s1 == s2:
        return True
    else:
        return False


print(lines_are_parallel([0,1,5], [0,1,5]))
