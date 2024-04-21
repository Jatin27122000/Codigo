# Write a Python program to create a decorator function to measure the execution time of a function.
import time

def jay(a,b):
    start=time.time();
    total=a+b
    print(time.time()-start)
    

a=45
b=75
jay(a,b)

@jay