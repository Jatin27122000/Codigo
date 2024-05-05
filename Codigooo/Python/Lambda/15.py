'''Write a  Python program to add two given lists using map and lambda.
Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
[5, 7, 9]'''

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, list1, list2))
print("Result: after adding two lists")
print(result)
