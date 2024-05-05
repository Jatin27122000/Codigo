
dict = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}

for key, value in dict.items():
    dict[key] = [v + 1 for v in value]

print("Original Dictionary:")
print(dict)
