''' Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.'''

try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
