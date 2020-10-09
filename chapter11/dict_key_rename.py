existing_dict = {'x': 1, 'y': 2, 'z': 3, 'd': 4}
old_key_new_key_map_dict = {'x': 'a', 'y': 'b', 'z': 'c'}

new_dict = dict((old_key_new_key_map_dict[key], value) for (key, value) in existing_dict.items())


print(existing_dict)
print(new_dict)
