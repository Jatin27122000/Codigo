''' Write a Python function to find the kth smallest element in a list.'''


def kth_smallest_el(lst, k):
    lst.sort()
    return lst[k - 1]

nums = [3, 2, 4, 3, 5, 4, 6, 9, 2, 7]

print("Original list:")
print(nums)

k = 1

for i in range(1, 11):
    print("kth smallest element in the said list, when k =", k)
    
    print(kth_smallest_el(nums, k))
    k = k + 1
