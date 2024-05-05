'''Write a  Python program to calculate the sum of harmonic series upto n terms.
Note: The harmonic sum is the sum of reciprocals of the positive integers.
Example :
harmonic series'''

def harmonic_series(n):
    if n == 1:
        return 1
    else:
        return 1 / n + harmonic_series(n - 1)

n = 5
print(f"The sum of the harmonic series up to {n} terms:", harmonic_series(n))
