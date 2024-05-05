'''Write a  Python program to append items from inerrable to the end of the array.
Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Extended array: array('i', [1, 3, 5, 7, 9, 1, 3, 5, 7, 9])'''

from array import array

arra = array('i', [1, 3, 5, 7, 9])
print("Original array:", arra)
iterable = [1, 3, 5, 7, 9]
arra.extend(iterable)
print("Extended array:", arra)