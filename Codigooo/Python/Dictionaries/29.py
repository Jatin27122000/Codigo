"""
 Write a Python program to remove spaces from dictionary keys.
"""

my_dict = {'a b c': [2, 3, 5],
           'b d e': [1, 8, 4],
           'c f g': [9, 0, 1]}

for key in my_dict:
    new_key = key.replace(' ', '')
    my_dict[new_key] = my_dict.pop(key)
print(my_dict)