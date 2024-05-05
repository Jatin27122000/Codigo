'''Write a  Python program to find out if a given array of integers contains any duplicate elements. Return true if any value appears at least twice in the array, and return false if every element is distinct.
Sample Output:
False
True
True'''

def contains_duplicates(arra):
    seen = set()
    
    for num in arra:
        if num in seen:
            return True
        seen.add(num)
    
    return False

print(contains_duplicates([11, 12, 13, 24, 35]))  
print(contains_duplicates([11, 12, 13, 34, 21]))  
print(contains_duplicates([21, 31, 32, 32, 13]))  
