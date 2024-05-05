''' Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.'''

def divide(x, y):
    try:
        result = x / y
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero!")

try:
    divide(10, 0)
except ZeroDivisionError:
    print("Error occurred while dividing numbers.")
