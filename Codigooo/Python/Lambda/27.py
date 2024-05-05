'''Write a  Python program to sort each sublist of strings in a given list of lists using lambda.
Original list:
[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
After sorting each sublist of the said list of lists:
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]'''

original_list = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
sorted_lists = list(map(lambda x: sorted(x), original_list))

print("Original list:")
print(original_list)
print("After sorting each sublist of the said list of lists:")
print(sorted_lists)
