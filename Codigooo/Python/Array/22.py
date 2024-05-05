'''Write a Python program that reads a string and interprets it as an array of machine values.
Sample Output:
array1: array('i', [7, 8, 9, 10])
Bytes: b'0700000008000000090000000a000000'
array2: array('i', [7, 8, 9, 10])'''

from array import array

bytes_string = b'0700000008000000090000000a000000'
array1 = array('i')
array1.frombytes(bytes_string)
print("array1:", array1)
bytes_array1 = array1.tobytes()
print("Bytes:", bytes_array1)
array2 = array('i')
array2.frombytes(bytes_array1)
print("array2:", array2)
