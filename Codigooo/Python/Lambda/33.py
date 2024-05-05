'''Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda.
Input the string: W3resource
['Valid string.']'''

input_string = input("Input the string: ")
valid_string = ['Valid string.'] if any(char.isupper() for char in input_string) \
                                   and any(char.islower() for char in input_string) \
                                   and any(char.isdigit() for char in input_string) \
                                   and len(input_string) >= 8 else []


print(valid_string)
