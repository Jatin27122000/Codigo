#Write a Python program to remove duplicates from a list.

a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
new=[]

for i in a:
    if i not in new:
        new.append(i)
print(new)    
    
    
'''2 method 
    l =[1,2,3,4,5,3]
    s=set(l)
print(list(s))
'''