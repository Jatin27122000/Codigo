'''Write a  Python program to rearrange positive and negative numbers in a given array using Lambda.
Original arrays:
[-1, 2, -3, 5, 7, 8, 9, -10]
Rearrange positive and negative numbers of the said array:
[2, 5, 7, 8, 9, -10, -3, -1]'''

original_array = [-1, 2, -3, 5, 7, 8, 9, -10]
rearranged_array = sorted(original_array, key=lambda x: (x >= 0, x))
print("Rearrange positive and negative numbers of the said array:")
print(rearranged_array)
