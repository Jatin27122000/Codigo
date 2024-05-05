'''Write a  Python program that removes all duplicate elements from an array and returns a new array.
Sample Output:
Original array: 1 3 5 1 3 7 9
After removing duplicate elements from the said array: 1 3 5 7 9
Original array: 2 4 2 6 4 8
After removing duplicate elements from the said array: 2 4 6 8'''

from array import array

def remove_duplicates(arr):
    return array(arr.typecode, set(arr))

arr1 = array('i', [1, 3, 5, 1, 3, 7, 9])
print("Original array:", ' '.join(map(str, arr1)))
print("After removing duplicate elements from the said array:", ' '.join(map(str, remove_duplicates(arr1))))

arr2 = array('i', [2, 4, 2, 6, 4, 8])
print("Original array:", ' '.join(map(str, arr2)))
print("After removing duplicate elements from the said array:", ' '.join(map(str, remove_duplicates(arr2))))