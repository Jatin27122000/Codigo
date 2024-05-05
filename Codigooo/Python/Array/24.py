'''Write a  Python program to find the missing number in a given array of numbers between 10 and 20.
Sample Output:
Original array: 10 11 12 13 14 16 17 18 19 20
Missing number in the said array (10-20): 15
Original array: 10 11 12 13 14 15 16 17 18 19
Missing number in the said array (10-20): 20'''

def find_missing_number(arra):
    all_numbers = set(range(10, 21))
    arr_numbers = set(arra)
    missing_number = all_numbers - arr_numbers
    
    return missing_number.pop() if missing_number else None

arr1 = [10, 11, 12, 13, 14, 16, 17, 18, 19, 20]
print("Original array:", ' '.join(map(str, arr1)))
print("Missing number in the said array (10-20):", find_missing_number(arr1))

arr2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print("Original array:", ' '.join(map(str, arr2)))
print("Missing number in the said array (10-20):", find_missing_number(arr2))