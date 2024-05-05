'''Write a Python program to count float values in a mixed list using lambda.
Original list:
[1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
Number of floats in the said mixed list:
3'''

original_list = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
count_floats = len(list(filter(lambda x: isinstance(x, float), original_list)))
print("Original list:")
print(original_list)
print("Number of floats in the said mixed list:")
print(count_floats)
