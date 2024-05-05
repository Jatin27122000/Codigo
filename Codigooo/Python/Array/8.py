'''Write a Python program to convert an array to an array of machine values and return the bytes representation.
Sample Output:
Bytes to String:
b'w3resource' '''

from array import array

arra = array('b', [119, 51, 114, 101, 115, 111, 117, 114, 99, 101])
bytes_representation = arra.tobytes()
string_representation = bytes_representation.decode()
print("Bytes to String:")
print(string_representation)
