#Write a Python program to convert a pair of values into a sorted unique array.

l = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
s=sorted(set().union(*l))
print(list(s))