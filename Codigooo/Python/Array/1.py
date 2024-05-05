'''Write a  Python program to create an array of 5 integers and display the array items. Access individual elements through indexes.
Sample Output:
1
3
5
7
9
Access first three items individually
1
3
5'''

from array import array

arra = array('i', [1, 3, 5, 7, 9])
for item in arra:
    print(item)
print("Access first three items individually")
for i in range(3):
    print(arra[i])
