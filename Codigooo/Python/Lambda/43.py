'''Write a Python program to multiply all the numbers in a given list using lambda.
Original list:
[4, 3, 2, 2, -1, 18]
Mmultiply all the numbers of the said list: -864
Original list:
[2, 4, 8, 8, 3, 2, 9]
Mmultiply all the numbers of the said list: 27648'''

from functools import reduce

list1 = [4, 3, 2, 2, -1, 18]
list2 = [2, 4, 8, 8, 3, 2, 9]
product1 = reduce(lambda x, y: x * y, list1)
product2 = reduce(lambda x, y: x * y, list2)

print("Original list:", list1)
print("Multiply all the numbers of the said list:", product1)
print("Original list:", list2)
print("Multiply all the numbers of the said list:", product2)
