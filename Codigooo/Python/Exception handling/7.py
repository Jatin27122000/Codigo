'''Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt 
 exception if the user cancels the input.'''

try:
    number = input("Enter a number: ")
    number = float(number)
    print("Entered number:", number)
except KeyboardInterrupt:
    print("\nInput canceled by user.")
except ValueError:
    print("Error: Please enter a valid number.")
