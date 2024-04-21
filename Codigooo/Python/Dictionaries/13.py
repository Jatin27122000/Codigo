"""
Write a Python program to map two lists into a dictionary.
"""

list_one = ['a', 'b', 'c', 'd']
list_two = [1, 2, 3, 4]
my_dict = dict(zip(list_one, list_two))
print(my_dict)