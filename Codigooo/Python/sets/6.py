"""
6. Write a Python program to create an intersection of sets.
"""
set_one = {'a', 'b', 'c'}
set_two = {'a', 'x', 'f'}

set_inter1 = set_one.intersection(set_two)
set_inter2 = set_one & set_two

print(set_inter1)
print(set_inter2)
