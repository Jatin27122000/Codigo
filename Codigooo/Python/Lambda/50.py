''' Write a  Python program to remove specific words from a given list using lambda.
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']
Remove words:
['orange', 'black']
After removing the specified words from the said list:
['red', 'green', 'blue', 'white']'''

original_list = ['orange', 'red', 'green', 'blue', 'white', 'black']
words_to_remove = ['orange', 'black']
filtered_list = list(filter(lambda x: x not in words_to_remove, original_list))

print("Original list:")
print(original_list)
print("Remove words:")
print(words_to_remove)
print("After removing the specified words from the said list:")
print(filtered_list)
