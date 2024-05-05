''' Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.'''

my_list = [1, 2, 3, 4, 5]

try:
    index = int(input("Enter the index to access: "))
    result = my_list[index]
    print("Element at index", index, ":", result)
except IndexError:
    print("Error: Index is out of range.")
except ValueError:
    print("Error: Please enter a valid integer.")
 