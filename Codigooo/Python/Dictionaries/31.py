# Write a Python program to get the key, value and item in a dictionary.


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 5, 'x': 2}

for k, v in my_dict.items():
    print('key:', k, 'value:', v, 'item:', (k, v))
