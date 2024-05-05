'''Write a Python program that implements a decorator to handle exceptions raised by a function and provide a default response.'''

import functools

def handle_exceptions(default_response):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Exception caught while executing '{func.__name__}': {e}")
                print("Returning default response:", default_response)
                return default_response
        return wrapper
    return decorator

@handle_exceptions(default_response="An error occurred")
def divide(a, b):
    return a / b

result = divide(10, 0)
print("Result:", result)
