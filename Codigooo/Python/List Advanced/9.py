'''Write a Python a function to find the maximum sum sub-sequence in a list. Return the maximum value.'''

def max_sum_subsequence(a):
    if not a:
        return 0
    
    max_sum = max_ending = a[0]
    
    for num in a[1:]:
        max_ending = max(num, max_ending + num)
        max_sum = max(max_sum, max_ending)
    
    return max_sum

my_list = [1, -3, 2, 1, -1, 4, -2, 3,8]
print(max_sum_subsequence(my_list))  
