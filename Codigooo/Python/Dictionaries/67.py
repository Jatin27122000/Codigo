
dict = {'Ora Mckinney': 8, 'Mathew Gilbert': 8, 'Theodore Hollandl': 7, 'Mae Fleming': 7, 'Ivan Little': 7}

idict = {}
for key, value in dict.items():
    idict.setdefault(value, []).append(key)

print("Inverted Dictionary:")
print(idict)
