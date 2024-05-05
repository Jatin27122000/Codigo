''' Write a Python program that implements a decorator to provide caching with expiration time for a function.'''

import time
import functools

def cache_with_expiry(expiration_time):
    def decorator(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            if key in cache:
                result, timestamp = cache[key]
                if time.time() - timestamp < expiration_time:
                    print(f"Using cached result for '{func.__name__}'")
                    return result
            result = func(*args, **kwargs)
            cache[key] = (result, time.time())
            return result
        return wrapper
    return decorator

@cache_with_expiry(expiration_time=5)  
def some_function(n):
    print(f"Calculating result for {n}")
    return n * n

print(some_function(5))  
print(some_function(5))  
time.sleep(6)  
print(some_function(5)) 
