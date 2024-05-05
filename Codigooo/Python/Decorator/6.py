'''Write a Python program that implements a decorator to retry a function multiple times in case of failure.'''

import time

def retry(times=3, delay=1):
    def decorator_retry(func):
        def wrapper_retry(*args, **kwargs):
            for attempt in range(times):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Attempt {attempt+1} failed:", e)
                    if attempt < times - 1:
                        time.sleep(delay)
                    else:
                        raise
        return wrapper_retry
    return decorator_retry

@retry(times=5, delay=2)
def risky_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Something went wrong!")
    else:
        return "Success!"

try:
    print(risky_function())
except Exception as e:
    print("Failed after retries:", e)
