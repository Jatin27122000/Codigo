''' Write a Python program that implements a decorator to cache the result of a function.'''

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print("Using cached result for arguments:", args)
            return cache[args]
        else:
            print("Computing result for arguments:", args)
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(5):", fibonacci(5))
print("Fibonacci(7):", fibonacci(7))
print("Fibonacci(5):", fibonacci(5))
