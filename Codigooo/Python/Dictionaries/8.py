# Write a Python script to merge two Python dictionaries.


dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict_two = {'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 0}

combined_dict = {}
combined_dict.update(dict_one, **dict_two)
print(combined_dict)