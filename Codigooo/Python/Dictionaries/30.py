""" Write a Python program to get the top three items in a shop.
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30,
'item4':55, 'item5': 24}
Expected Output: 
item4 55
item1 45.5
item3 41.3
"""

items_dict = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

my_list = [(k, v) for k,v in items_dict.items()]
my_list.sort(key=lambda x: x[1], reverse=True)
for i in my_list[:3]:
    print('{:<5s}'.format(i[0]), '{:<5.2f}'.format(i[1]))

