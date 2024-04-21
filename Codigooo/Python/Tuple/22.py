my_list = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

new_list = [i for i in my_list if i]
print(new_list)