
dic = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}


dicl = [{key: values[i] for key, values in dic.items()} for i in range(len(list(dic.values())[0]))]
print(dicl)
