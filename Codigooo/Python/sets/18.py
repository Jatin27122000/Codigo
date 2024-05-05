
set1 = {1, 2, 3, 4}
if set1.issuperset(set1):
    print("The set is a superset of itself.")
else:
    print("The set is not a superset of itself.")


set2 = {2, 3}
if set1.issuperset(set2):
    print("The set is a superset of the other set.")
else:
    print("The set is not a superset of the other set.")
