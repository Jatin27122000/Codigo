'''Write a  Python program to calculate the product of a given list of numbers using lambda.
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Product of the said list numbers:
3628800
list2: [2.2, 4.12, 6.6, 8.1, 8.3]
Product of the said list numbers:
4021.8599520000007'''

from functools import reduce

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2.2, 4.12, 6.6, 8.1, 8.3]

product1 = reduce(lambda x, y: x * y, list1)
product2 = reduce(lambda x, y: x * y, list2)

print("list1:", list1)
print("Product of the said list numbers:", product1)
print("list2:", list2)
print("Product of the said list numbers:", product2)
