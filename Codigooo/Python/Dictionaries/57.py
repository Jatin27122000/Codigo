
dict1 = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
dict2 = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}

fdict1 = {key: [num for num in value if num % 2 == 0] for key, value in dict1.items()}
fdict2 = {key: [num for num in value if num % 2 == 0] for key, value in dict2.items()}

print("Original Dictionary:")
print(dict1)
print("Filter even numbers from said dictionary values:")
print(fdict1)
print("\nOriginal Dictionary:")
print(dict2)
print("Filter even numbers from said dictionary values:")
print(fdict2)
