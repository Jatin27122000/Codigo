'''Write a  Python program to find the index position and value of the maximum and minimum values in a given list of numbers using lambda.
Original list:
[12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
Index position and value of the maximum value of the said list:
(5, 89)
Index position and value of the minimum value of the said list:
(3, 10.11)'''

original_list = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
max_index, max_value = max(enumerate(original_list), key=lambda x: x[1])
min_index, min_value = min(enumerate(original_list), key=lambda x: x[1])

print("Original list:")
print(original_list)
print("Index position and value of the maximum value of the said list:")
print((max_index, max_value))
print("Index position and value of the minimum value of the said list:")
print((min_index, min_value))
