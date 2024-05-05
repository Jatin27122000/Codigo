
list = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]


subject = 'Math' 
values_list = [d[subject] for d in list]


print("Original Dictionary:")
print(list)
print(f"Extract a list of values from said list of dictionaries where subject = {subject}:")
print(values_list)
