''' Write a  Python program to convert string elements to integers inside a given tuple using lambda.
Original tuple values:
(('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
New tuple values:
((233, 33), (1416, 55), (2345, 34))'''

original_tuple = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
new_tuple = tuple(map(lambda x: tuple(map(int, filter(str.isdigit, x))), original_tuple))
print("Original tuple values:")
print(original_tuple)
print("New tuple values:")
print(new_tuple)
