"""
 Write a Python program to sort a list alphabetically in a dictionary.
"""

my_dict = {'a': [2, 3, 5],
           'b': [1, 8, 4],
           'c': [9, 0, 1]}

for li in my_dict.values():
    li.sort()
print(my_dict)