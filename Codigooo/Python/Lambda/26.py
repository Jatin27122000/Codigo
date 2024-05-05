'''Write a Python program to find a list with maximum and minimum length using lambda.
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])'''

original_list = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
max_length_list = max(original_list, key=lambda x: len(x))
min_length_list = min(original_list, key=lambda x: len(x))

print("Original list:")
print(original_list)
print("List with maximum length of lists:")
print((len(max_length_list), max_length_list))
print("List with minimum length of lists:")
print((len(min_length_list), min_length_list))
