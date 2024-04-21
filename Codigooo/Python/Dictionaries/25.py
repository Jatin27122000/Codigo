"""
 Write a Python program to print a dictionary in table format.
"""

my_dict = {'alice': 11, 'benji': 24, 'cilian': 38, 'david': 42, 'ewan': 56}

for key, value in my_dict.items():
    print('{:<7s}'.format(key), '{:>3d}'.format(value))
