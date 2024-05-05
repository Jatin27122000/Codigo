'''Write a  Python program to check whether a specified list is sorted or not using lambda.
Original list:
[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
Is the said list is sorted!
True
Original list:
[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
Is the said list is sorted!
False'''

is_sorted = lambda lst: all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
original_list = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
result = is_sorted(original_list)
print("Original list:")
print(original_list)
print("Is the said list sorted?")
print(result)
