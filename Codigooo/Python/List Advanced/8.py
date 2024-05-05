''' Write a Python function to remove duplicates from a list while preserving the order.'''

my_list = [1, 2, 3, 2, 4, 1, 5]
seen = set()
unique_list = []

for item in my_list:
    if item not in seen:
        seen.add(item)
        unique_list.append(item)

print(unique_list)  
