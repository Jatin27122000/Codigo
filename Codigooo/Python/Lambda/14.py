'''Write a  Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda.
Sample Output:
Monday
Friday
Sunday'''

original_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
filtered_list = list(filter(lambda x: len(x) == 6, original_list))
print("Sample Output:")
for value in filtered_list:
    print(value)
