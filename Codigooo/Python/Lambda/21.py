'''Write a  Python program that multiplies each number in a list with a given number using lambda functions. Print the results.
Original list: [2, 4, 6, 9, 11]
Given number: 2
Result:
4 8 12 18 22'''

original_list = [2, 4, 6, 9, 11]
given_number = 2
result = list(map(lambda x: x * given_number, original_list))

print("Original list:", original_list)
print("Given number:", given_number)
print("Result:")
print(*result)

