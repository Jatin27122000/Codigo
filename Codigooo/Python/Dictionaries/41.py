
dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}

# Drop empty items
new_dict = {key: value for key, value in dict.items() if value is not None}

# Print the new dictionary
print("Original Dictionary:")
print(dict)
print("New Dictionary after dropping empty items:")
print(new_dict)
