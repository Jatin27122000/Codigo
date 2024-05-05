'''Write a  Python program to insert a newly created item before the second element in an existing array.
Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Insert new value 4 before 3:
New array: array('i', [1, 4, 3, 5, 7, 9])'''

from array import array

arra = array('i', [1, 3, 5, 7, 9])
print("Original array:", arra)
new_value = 4
arra.insert(1, new_value)
print("Insert new value", new_value, "before", arra[1], ":")
print("New array:", arra)