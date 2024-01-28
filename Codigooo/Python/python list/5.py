'''Write a Python program to count the number of strings from a given list of strings. 
The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2'''

l=['abc', 'xyz', 'aba', '1221']
j=0
for i in l:
    if len(i)>=2 and i[0]==i[-1]:
        j+=1
print(j)