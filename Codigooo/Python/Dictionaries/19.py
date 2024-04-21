
dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}
for key in dict2:
	if key in dict1:
		dict2[key] = dict2[key] + dict1[key]
	else:
		pass
		
print(dict2)
