"""
1. Write a Python script to sort (ascending and descending) a dictionary
by value.
"""

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
    
