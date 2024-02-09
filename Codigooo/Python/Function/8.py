#Write a Python function that takes a list and returns a new list with distinct elements from the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def fun(l):
 
    s=set(l)
    print(list(s))

l =[1,2,3,3,3,3,4,5]
fun(l)