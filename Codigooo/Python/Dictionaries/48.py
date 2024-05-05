
list = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

id = '#FF0000'

nlist = [d for d in list if d['id'] != id]
print(f"Remove id {id} from the said list of dictionary:")
print(nlist)
