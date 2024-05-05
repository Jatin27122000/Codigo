''' Write a Python program to get array buffer information.
Sample Output:
Array buffer start address in memory and number of elements.
(140023105054240, 2)'''

from array import array

arra = array('i', [20, 10])
buffer_info = arra.buffer_info()
print("Array buffer start address in memory and number of elements:")
print(buffer_info)
