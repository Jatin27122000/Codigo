
d1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
d2 = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

l1 = [[key, value] for key, value in d1.items()]
l2 = [[key, value] for key, value in d2.items()]

print("Original Dictionary:")
print(d1)
print("Convert the said dictionary into a list of lists:")
print(l1)
print("\nOriginal Dictionary:")
print(d2)
print("Convert the said dictionary into a list of lists:")
print(l2)
