#Write a Python function to find the maximum of three numbers.
def max(a, b, c): 
 
    if (a >= b) and (a >= c): 
        l=a 
    elif (b >= a) and (b >= c): 
        l=b 
    else:
        (c >= a) and (c >= b)
        l=c
    return l
        
a = 10
b = 14
c = 12
print(max(a, b, c)) 