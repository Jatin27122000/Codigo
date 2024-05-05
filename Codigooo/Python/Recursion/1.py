'''Write a  Python program to calculate the sum of a list of numbers using recursion.'''

def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])

numbers = [1, 2, 3, 4, 5]
print("Sum of the list:", recursive_sum(numbers))
