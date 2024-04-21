
ids = ['S001', 'S002', 'S003', 'S004']
names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
scores = [85, 98, 89, 92]

# Convert lists to a nested dictionary
nested_dict = [{id_: {name: score}} for id_, name, score in zip(ids, names, scores)]


print("Original strings:")
print(ids)
print(names)
print(scores)
print("\nNested dictionary:")
print(nested_dict)


    
