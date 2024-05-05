
list = [
    [1, 'Jean Castro', 'V'],
    [2, 'Lula Powell', 'V'],
    [3, 'Brian Howell', 'VI'],
    [4, 'Lynne Foster', 'VI'],
    [5, 'Zachary Simon', 'VII']
]

converted_dict = {sublist[0]: sublist[1:] for sublist in list}

print("Convert the said list of lists to a dictionary:")
print(converted_dict)
