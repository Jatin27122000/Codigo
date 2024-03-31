#Write a Python program to extract a given number of randomly selected elements from a given list.


import random
l = [2, 2, 4, 6, 6, 8]
n = 5
print(random.sample(l, n))