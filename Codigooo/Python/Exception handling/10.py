''' Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.'''

try:
    my_list = [1, 2, 3]
    print("Length of list:", len(my_list))
    
    my_list.non_existent_attribute
except AttributeError:
    print("Error: Attribute does not exist.")
