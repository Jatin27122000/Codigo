my_tuple = (1, 1, 2, 3, 4, 4, 5)

repeated_items = []
for i in my_tuple:
    if my_tuple.count(i) > 1:
        repeated_items.append(i)
print(set(repeated_items))