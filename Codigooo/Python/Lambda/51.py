'''Write a  Python program to find the maximum and minimum values in a given list of tuples using the lambda function.
Original list with tuples:
[('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
Maximum and minimum values of the said list of tuples:
(74, 62)'''

original_list = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
max_value = max(original_list, key=lambda x: x[1])[1]
min_value = min(original_list, key=lambda x: x[1])[1]

print("Original list with tuples:")
print(original_list)
print("Maximum and minimum values of the said list of tuples:")
print((max_value, min_value))
