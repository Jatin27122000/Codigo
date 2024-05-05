'''  Write a Python program to remove None values from a given list using the lambda function.
Original list:
[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
Remove None value from the said list:
[12, 0, 23, -55, 234, 89, 0, 6, -12]'''

original_list = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
filtered_list = list(filter(lambda x: x is not None, original_list))

print("Original list:")
print(original_list)
print("Remove None value from the said list:")
print(filtered_list)
