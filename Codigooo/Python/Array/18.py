'''Write a  Python program to create an array of six integers. Print all members of the array.
Sample Output:
10
20
30
40
50
60'''

from array import array

arra = array('i', [10, 20, 30, 40, 50, 60])
for num in arra:
    print(num)
