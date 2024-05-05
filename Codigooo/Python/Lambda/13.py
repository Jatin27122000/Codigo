'''Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array: 3
Number of odd numbers in the above array: 5'''

original_array = [1, 2, 3, 5, 7, 8, 9, 10]
even_count = len(list(filter(lambda x: x % 2 == 0, original_array)))
odd_count = len(list(filter(lambda x: x % 2 != 0, original_array)))
print("Number of even numbers in the above array:", even_count)
print("Number of odd numbers in the above array:", odd_count)
