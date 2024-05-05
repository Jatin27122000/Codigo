'''Write a Python a function to find the union and intersection of two lists.'''

l1 = [13, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

u = list(set(l1 + l2))
print("Union:", u)

i = list(set(l1) & set(l2))
print("Intersection:", i)


