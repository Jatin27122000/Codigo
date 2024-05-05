'''Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.'''

try:
    dividend = float(input("Enter the dividend: "))
    divisor = float(input("Enter the divisor: "))
    result = dividend / divisor
    print("Result of division:", result)
except ArithmeticError:
    print("Error: Arithmetic error occurred.")
except ValueError:
    print("Error: Please enter valid numerical values.")
