''' Write a Python program that implements a decorator to enforce type checking on the arguments of a function.'''

import functools

def enforce_types(*arg_types, **kwarg_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i, arg in enumerate(args):
                if i < len(arg_types) and not isinstance(arg, arg_types[i]):
                    raise TypeError(f"Argument at position {i} must be of type {arg_types[i].__name__}")
            for kwarg, kwarg_type in kwarg_types.items():
                if kwarg in kwargs and not isinstance(kwargs[kwarg], kwarg_type):
                    raise TypeError(f"Argument '{kwarg}' must be of type {kwarg_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@enforce_types(int, str, c=str)
def example_function(a, b, c):
    print("Arguments:", a, b, c)

try:
    example_function(10, "Hello", c=3.14)
except TypeError as e:
    print("Error:", e)
