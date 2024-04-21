my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 5}

new_dict = {}

for key, value in my_dict.items():
    if value not in new_dict.values():
        new_dict[key] = value

print(new_dict)