#Write a Python program to find common items in two lists.

a = [1, 2, 3, 4]
b = [1, 9, 5, 6,4]
s=set(a)
t=set(b)

z = s.intersection(t)
print(z)
