"""
13. Write a Python program to use of frozensets.
"""

x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])
print(x.isdisjoint(y))
print(x.difference(y))
print(x | y)
