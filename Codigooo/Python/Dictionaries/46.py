
original_list = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]


grouped_dict = {}
for key, value in original_list:
    grouped_dict.setdefault(key, []).append(value)

print("Grouping a sequence of key-value pairs into a dictionary of lists:")
print(grouped_dict)
