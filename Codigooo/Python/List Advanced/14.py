'''Write a Python function to sort a list of dictionaries based on values of a key.'''

def sort_list_of_dicts(list_of_dicts, key):
    
    return sorted(list_of_dicts, key=lambda x: x[key])

data = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 20}]
sorted_data = sort_list_of_dicts(data, 'age')
print(sorted_data)
