my_dict = {'a': [2, 3, 5],
           'b': [1, 8, 4],
           'c': [9, 0, 1]}

my_new_dict = {k: sum(v) for k, v in my_dict.items()}
print(my_new_dict)