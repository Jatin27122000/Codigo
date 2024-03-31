# Write a Python program to get the frequency of elements 
# in a list.
l = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
fre = {}

for i in l:
   
   if i in fre:
        fre[i] += 1
   else:
     
        fre[i] = 1
print(fre)