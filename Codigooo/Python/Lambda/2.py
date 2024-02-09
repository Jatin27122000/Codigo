'''Write a Python program to create a function that takes one argument, and that argument will be
multiplied with an unknown given number.
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75
'''

def fun(n):
    r=lambda a:a*n
    return r
t=fun(2)
print(t(15))
t=fun(3)
print(t(15))
t=fun(4)
print(t(15))
t=fun(5)
print(t(15))


