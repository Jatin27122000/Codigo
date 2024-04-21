"""
Write a Python program to print all unique values in a dictionary.
Sample Data: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
            {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
Expected Output: Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
            {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

my_set = set()
for dictionary in my_list:
    for k, v in dictionary.items():
        my_set.add(v)
print(my_set)