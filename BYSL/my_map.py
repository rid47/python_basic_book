def to_upper_case(s):
    return str(s).upper()


# utility function to print map

def print_iterator(it):
    for x in it:
        print(x, end='')
    print('')


map_iterator = map(to_upper_case, 'abc')
print(type(map_iterator))
print_iterator(map_iterator)
