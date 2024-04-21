my_list = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

my_list.sort(key=lambda x: x[1], reverse=True)
print(my_list)