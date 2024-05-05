'''Write a  Python program to extract the nth element from a given list of tuples using lambda.
Original list:
[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
Extract nth element ( n = 0 ) from the said list of tuples:
['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
Extract nth element ( n = 2 ) from the said list of tuples:
[99, 96, 94, 98]'''


original_list = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
n = 0 
extracted_elements = list(map(lambda x: x[n], original_list))
print("Original list:")
print(original_list)
print(f"Extract nth element (n = {n}) from the said list of tuples:")
print(extracted_elements)
