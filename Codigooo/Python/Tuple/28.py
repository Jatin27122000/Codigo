
original_tuple = (('333', '33'), ('1416', '55'))

new_tuple = tuple(tuple(int(x) for x in tup) for tup in original_tuple)

# Print the new tuple values
print("Original tuple values:")
print(original_tuple)
print("New tuple values:")
print(new_tuple)



#nhi smzra