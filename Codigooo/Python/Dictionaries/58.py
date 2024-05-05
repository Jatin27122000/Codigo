from itertools import combinations

dict1 = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
dict2 = {'V': [1, 3, 5], 'VI': [1, 5]}

cdict1 = [dict(combo) for r in range(1, len(dict1) + 1) for combo in combinations(dict1.items(), r)]
cdict2 = [dict(combo) for r in range(1, len(dict2) + 1) for combo in combinations(dict2.items(), r)]

print("Original Dictionary:")
print(dict1)
print("Combinations of key-value pairs of the said dictionary:")
print(cdict1)
print("\nOriginal Dictionary:")
print(dict2)
print("Combinations of key-value pairs of the said dictionary:")
print(cdict2)
