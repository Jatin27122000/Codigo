'''Write a  Python program that implements a decorator to enforce rate limits on a function.'''

import time

def rate_limit(limit_per_second):
    def decorator(func):
        last_called = 0
        def wrapper(*args, **kwargs):
            nonlocal last_called
            current_time = time.time()
            elapsed_time = current_time - last_called
            if elapsed_time < 1 / limit_per_second:
                raise Exception("Rate limit exceeded")
            else:
                result = func(*args, **kwargs)
                last_called = current_time
                return result
        return wrapper
    return decorator

@rate_limit(limit_per_second=2)
def some_function():
    print("Function called")

try:
    some_function()
    some_function()
    some_function()
except Exception as e:
    print("Error:", e)
