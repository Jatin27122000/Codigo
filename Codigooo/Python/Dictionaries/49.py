# for intiger
oi = [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]

ci = [{key: int(value) for key, value in d.items()} for d in oi]

print("Original list:")
print(oi)
print("String values of a given dictionary, into integer types:")
print(ci)


#for float
of = [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]

cf = [{key: float(value) for key, value in d.items()} for d in of]

print("Original list:")
print(of)
print("String values of a given dictionary, into float types:")
print(cf)
