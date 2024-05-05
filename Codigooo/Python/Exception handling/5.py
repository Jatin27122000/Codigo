''' Write a Python program that opens a file and handles a PermissionError exception if 
 there is a permission issue.'''


try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except PermissionError:
    print("Error: Permission denied. You do not have the necessary permissions to open the file.")
