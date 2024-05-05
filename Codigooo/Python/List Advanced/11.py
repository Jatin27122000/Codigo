'''Write a Python function to find the longest common sub-sequence in two lists.'''

def longest_common_subsequence(list1, list2):
    m = len(list1)
    n = len(list2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if list1[i - 1] == list2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if list1[i - 1] == list2[j - 1]:
            lcs.append(list1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return list(reversed(lcs))

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(longest_common_subsequence(list1, list2))  
