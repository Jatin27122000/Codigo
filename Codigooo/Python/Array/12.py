'''Write a  Python program to remove the first occurrence of a specified element from an array.
Sample Output:
Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
Remove the first occurrence of 3 from the said array:
New array: array('i', [1, 5, 3, 7, 1, 9, 3])'''

from array import array

arra = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array:", arra)
element_to_remove = 3
arra.remove(element_to_remove)
print("Remove the first occurrence of", element_to_remove, "from the said array:")
print("New array:", arra)