"""
14. Write a Python program to sort a dictionary by key.
"""

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for key in sorted(my_dict.keys()):
    print(key, ":", my_dict[key])