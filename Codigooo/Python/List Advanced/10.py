'''Write a Python a function to find the minimum sum sub-sequence in a list. Return the sub-sequence.'''

def min_sum_subsequence(arr):
    if not arr:
        return []

    min_sum = min_ending_here = arr[0]
    start = end = 0
    current_start = 0

    for i in range(1, len(arr)):
        if arr[i] < min_ending_here + arr[i]:
            min_ending_here = arr[i]
            current_start = i
        else:
            min_ending_here += arr[i]

        if min_ending_here < min_sum:
            min_sum = min_ending_here
            start = current_start
            end = i

    return arr[start:end+1]

my_list = [1, -3, 2, 1, -1, 4, -2, 3]
print(min_sum_subsequence(my_list))  
