"""
 Write a Python program to get the maximum and minimum value in a dictionary.
"""

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

dict_min = min(my_dict.values())
dict_max = max(my_dict.values())

print('in dictionary', my_dict, 'max is %d and min is %d' % (dict_max, dict_min))
