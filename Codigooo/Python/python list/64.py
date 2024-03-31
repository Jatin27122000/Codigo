# Write a Python program to iterate over two lists simultaneously.

import itertools

num = [1, 2, 3]
color = ['red', 'white', 'black']
for (a, b) in zip(num, color):
     print (a, b)