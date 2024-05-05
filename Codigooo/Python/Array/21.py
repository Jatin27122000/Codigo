'''Write a Python program to get the array size of types unsigned integer and float.
Sample Output:
4
4'''

from array import array

unsigned_int_array = array('I')
unsigned_int_size = unsigned_int_array.itemsize
float_array = array('f')
float_size = float_array.itemsize
print("Array size of unsigned integer:", unsigned_int_size)
print("Array size of float:", float_size)
