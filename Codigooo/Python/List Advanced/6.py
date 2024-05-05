''' Write a Python function to check if a list is a palindrome or not. Return true otherwise false.'''

my_list = [1, 2, 3, 2, 1]

is_palindrome = my_list == my_list[::-1]
print(is_palindrome)