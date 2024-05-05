'''Write a Python program to calculate the value of 'a' to the power of 'b' using recursion.
Test Data :
(power(3,4) -> 81'''

def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

a = 3
b = 4
print(f"The value of {a} to the power of {b}:", power(a, b))
