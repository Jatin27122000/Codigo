'''Write a Python program to solve the Fibonacci sequence using recursion.'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 10
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i), end=" ")
