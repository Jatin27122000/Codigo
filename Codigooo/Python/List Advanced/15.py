'''Write a Python program to find all the pairs in a list whose sum is equal to a given value.'''

def find_pairs_with_sum(arr, target_sum):
    pairs = []
    complement_map = {}

    for num in arr:
        complement = target_sum - num
        if complement in complement_map:
            pairs.append((num, complement))
        complement_map[num] = complement

    return pairs
my_list = [1, 2, 3, 4, 5, 6]
target_sum = 7
pairs = find_pairs_with_sum(my_list, target_sum)
print("Pairs with sum", target_sum, ":", pairs)
