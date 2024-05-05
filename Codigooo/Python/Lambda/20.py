'''Write a  Python program to find the numbers in a given string and store them in a list. Afterward, display the numbers that are longer than the length of the list in sorted form. Use the lambda function to solve the problem.
Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
Numbers in sorted form:
20 23 56'''

original_string = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
numbers_list = [int(s) for s in original_string.split() if s.isdigit()]
result = sorted(filter(lambda x: len(str(x)) > len(numbers_list), numbers_list))

print("Original string:", original_string)
print("Numbers in sorted form:")
print(*result)
