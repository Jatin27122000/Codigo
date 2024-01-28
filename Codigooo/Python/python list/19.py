#Write a Python program to calculate the difference between the two lists.

a=[1,3,5,7,9]
b=[1,2,4,6,7,8]
d=list(set(a)-set(b))
d1=list(set(b)-set(a))
total=d+d1

print(total)     
  