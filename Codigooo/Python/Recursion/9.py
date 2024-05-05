'''Write a Python program to calculate the geometric sum up to 'n' terms.
Note: In mathematics, a geometric series is a series with a constant ratio between successive terms.'''

def geometric_sum(a, r, n):
    if r == 1:
        return a * n
    else:
        return a * (1 - r**n) / (1 - r)

a = 4  
r = 0.5  
n = 2  
print(f"The geometric sum up to {n} terms:", geometric_sum(a, r, n))
