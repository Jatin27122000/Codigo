dict= {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}

skey = min(dict, key=lambda k: len(dict[k]))
slist = [skey]

print(slist)