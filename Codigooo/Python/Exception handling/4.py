''' Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.'''

def numeric_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            numeric_value = float(user_input)  
            return numeric_value
        except ValueError:
            print("Error: Please enter a numerical value.")

try:
    num1 = numeric_input("Enter the first number: ")
    num2 = numeric_input("Enter the second number: ")
    print("First number:", num1)
    print("Second number:", num2)
except TypeError:
    print("Error occurred while getting numerical input.")
