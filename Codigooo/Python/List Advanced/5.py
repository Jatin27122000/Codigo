'''Write a Python function to find the kth largest element in a list.'''

def kth_largest(a, k):
    
    if k < 0 or k >= len(a):
        print("Error: Index k is out of range.")
        return None
    
    return max(sorted(a, reverse=True)[:k+1])

my_list = [3, 1, 4, 2, 5,7,9]
k = 2
result = kth_largest(my_list, k)
if result is not None:
    print(f"The {k+1}rd largest element in the list is: {result}")
