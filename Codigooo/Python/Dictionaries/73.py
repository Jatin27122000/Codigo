
list = [
    {'name': 'Theodore', 'age': 18},
    {'name': 'Mathew', 'age': 22},
    {'name': 'Roxanne', 'age': 20},
    {'name': 'David', 'age': 18}
]

specified_key = 'age'
values_list = [d[specified_key] for d in list]
print("List of values corresponding to the specified key:")
print(values_list)

