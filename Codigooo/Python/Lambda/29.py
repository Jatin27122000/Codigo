'''Write a Python program to find the maximum value in a given heterogeneous list using lambda.
Original list:
[' Python', 3, 2, 4, 5, 'version']
Maximum values in the said list using lambda:
5'''

original_list = [' Python', 3, 2, 4, 5, 'version']
max_value = max(original_list, key=lambda x: float('inf') if isinstance(x, str) else x)

print("Original list:")
print(original_list)
print("Maximum values in the said list using lambda:")
print(max_value)
