'''Write a  Python program to find the greatest common divisor (GCD) of two integers using recursion.'''

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = 56
b = 39
print(f"The GCD of {a} and {b} is:", gcd(a, b))
