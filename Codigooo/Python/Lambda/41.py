'''Write a  Python program to reverse strings in a given list of string values using lambda.
Original lists:
['Red', 'Green', 'Blue', 'White', 'Black']
Reverse strings of the said given list:
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']'''

original_list = ['Red', 'Green', 'Blue', 'White', 'Black']
reversed_list = list(map(lambda x: x[::-1], original_list))

print("Original list:")
print(original_list)
print("Reverse strings of the said given list:")
print(reversed_list)


