'''Write a Python function find the length of the longest increasing sub-sequence in a list.'''

def longest_length(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_length(nums))  
