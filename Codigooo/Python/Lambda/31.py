'''Write a  Python program to extract a specified size of strings from a given list of string values using lambda.
Original list:
[' Python', 'list', 'exercises', 'practice', 'solution']
length of the string to extract:
8
After extracting strings of specified length from the said list:
['practice', 'solution']'''

original_list = [' Python', 'list', 'exercises', 'practice', 'solution']
length_to_extract = 8
extracted_strings = list(filter(lambda x: len(x.strip()) == length_to_extract, original_list))

print("Original list:")
print(original_list)
print("Length of the string to extract:")
print(length_to_extract)
print("After extracting strings of specified length from the said list:")
print(extracted_strings)
