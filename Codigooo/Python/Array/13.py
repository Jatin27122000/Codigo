'''Write a  Python program to convert an array to an ordinary list with the same items.
Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
Convert the said array to an ordinary list with the same items:
[1, 3, 5, 3, 7, 1, 9, 3]'''

from array import array

arra = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array:", arra)
ordinary_list = arra.tolist()
print("Convert the said array to an ordinary list with the same items:")
print(ordinary_list)