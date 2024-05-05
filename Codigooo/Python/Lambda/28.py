'''Write a  Python program to sort a given list of lists by length and value using lambda.
Original list:
[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
Sort the list of lists by length and value:
[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]'''

original_list = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
sorted_list = sorted(original_list, key=lambda x: (len(x), x))

print("Original list:")
print(original_list)
print("Sort the list of lists by length and value:")
print(sorted_list)
