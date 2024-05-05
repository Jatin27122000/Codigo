dict1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
dict2 = {'x': 300, 'y': 'Red', 'z': 600}
combined_dict = {}
for d in (dict1, dict2):
    for key, value in d.items():
        combined_dict.setdefault(key, []).append(value)

print(combined_dict)