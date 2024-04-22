"""
5. Write a Python program to remove an item from a set if it is present in the set.
"""

my_set = {'a', 'b'}
my_set.discard('a')
my_set.discard('c')
print(my_set)