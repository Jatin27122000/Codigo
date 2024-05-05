'''Write a  Python program to find a pair with the highest product from a given array of integers.
Original array: [1, 2, 3, 4, 7, 0, 8, 4]
Maximum product pair is: (7, 8)
Original array: [0, -1, -2, -4, 5, 0, -6]
Maximum product pair is: (-4, -6)'''

def maxProductPair(arra):
    if len(arra) < 2:
        return "Array should contain at least two elements"
    
    max_product = float('-inf')
    max_pair = ()
    
    for i in range(len(arra)):
        for j in range(i+1, len(arra)):
            product = arra[i] * arra[j]
            if product > max_product:
                max_product = product
                max_pair = (arra[i], arra[j])
    
    return max_pair

arr1 = [1, 2, 3, 4, 7, 0, 8, 4]
print("Original array:", arr1)
print("Maximum product pair is:", maxProductPair(arr1))

arr2 = [0, -1, -2, -4, 5, 0, -6]
print("Original array:", arr2)
print("Maximum product pair is:", maxProductPair(arr2))