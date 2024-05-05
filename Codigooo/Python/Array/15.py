'''Write a Python program to find the first duplicate element in a given array of integers. Return -1 if there are no such elements.
Sample Output:
4
-1
1'''

def first_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1

print(first_duplicate([11, 12, 13, 14, 14, 15]))  
print(first_duplicate([21, 22, 23, 24, 25]))     
print(first_duplicate([21, 21, 22, 23, 24]))     