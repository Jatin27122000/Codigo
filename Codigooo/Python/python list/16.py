'''Write a Python program to generate and print a list 
of the first and last 5 elements where the
values are square numbers between 1 and 30 (both included).'''

for i in range(1,31):
    if(i<=5) :
        print(i**2) 
    elif(i>25):
        print(i**2)