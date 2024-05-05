'''Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.'''

try:
    with open("example.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except UnicodeDecodeError:
    print("Error: Encoding issue. Unable to decode the file with the specified encoding.")
except FileNotFoundError:
    print("Error: File not found.")
