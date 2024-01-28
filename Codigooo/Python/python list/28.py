#Write a Python program to find the second largest number in a list.
l =[2,3,16,-5,66,55]
for i in l:
    l.sort()
    print(l[-2])
    break