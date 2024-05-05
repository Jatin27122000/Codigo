'''Write a  Python program to find the nested list elements, which are present in another list using lambda.
Original lists: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
Intersection of said nested lists:
[[12], [7, 11], [1, 5, 8]]'''

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nested_lists = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
intersection = [list(filter(lambda x: x in original_list, sublist)) for sublist in nested_lists]

print("Original list:")
print(original_list)
print("Nested lists:")
print(nested_lists)
print("Intersection of said nested lists:")
print(intersection)
 