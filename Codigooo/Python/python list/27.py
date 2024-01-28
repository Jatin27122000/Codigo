 #Write a Python program to find the second smallest number in a list
l =[2,3,16,-5,66]
for i in l:
    l.sort()
    print(l[1])
    break