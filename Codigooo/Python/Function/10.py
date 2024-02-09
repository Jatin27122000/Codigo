'''Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]'''

def even(n):
    a=[]
    for i in n:
        if  i%2==0:
            a.append(i)
    return a        
        
            

n=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print (even(n))