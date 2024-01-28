#Write a Python program to shuffle and print a specified list.

import random
l=[1,2,3,4,5,6]
print("original" , l)
random.shuffle(l)
print("shuffle" , l)