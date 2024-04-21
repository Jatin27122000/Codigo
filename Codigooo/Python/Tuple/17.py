
my_list = [(1, 2), ('a', 'b'), (True, False)]

unzipped_lists = list(zip(*my_list))

for lst in unzipped_lists:
    print(lst)
