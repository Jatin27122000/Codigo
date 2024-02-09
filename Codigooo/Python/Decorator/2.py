import time

def jay(a,b):
    start=time.time();
    total=a+b
    print(time.time()-start)
    return total

a=45
b=55351
jay(a,b)