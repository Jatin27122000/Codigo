'''Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using the lambda function.
Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
Sum of the positive numbers: -32
Sum of the negative numbers: 48'''

numbers_list = [2, 4, -6, -9, 11, -12, 14, -5, 17]
sum_positive = sum(filter(lambda x: x > 0, numbers_list))
sum_negative = sum(filter(lambda x: x < 0, numbers_list))

print("Original list:", numbers_list)
print("Sum of the positive numbers:", sum_positive)
print("Sum of the negative numbers:", sum_negative)
