''' Write a  Python program that implements a decorator to add logging functionality to a function.'''

import functools
import logging

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function '{func.__name__}' with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

logging.basicConfig(level=logging.INFO)

@logger
def add(a, b):
    return a + b

result = add(3, 5)
print("Result:", result)
