''' Write a  Python program to find the elements of a given list of strings that contain a specific substring using lambda.
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]'''

original_list = ['red', 'black', 'white', 'green', 'orange']
substring1 = 'ack'
substring2 = 'abc'

result1 = list(filter(lambda x: substring1 in x, original_list))
result2 = list(filter(lambda x: substring2 in x, original_list))

print("Original list:")
print(original_list)
print("Substring to search:", substring1)
print("Elements of the said list that contain specific substring:")
print(result1)
print("Substring to search:", substring2)
print("Elements of the said list that contain specific substring:")
print(result2)
