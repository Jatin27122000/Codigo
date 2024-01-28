#Write a Python function that takes two lists and returns True if they have at least one common member.



a = [1, 2, 3, 4]
b = [1, 9, 5, 6]
s=set(a)
t=set(b)

z = s.intersection(t)
if not z:
    print("The lists have no common members.")
else:
    print("The lists have at least one common member.")