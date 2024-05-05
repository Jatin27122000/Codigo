
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1 -= set1.intersection(set2)

print("Set 1 after removing intersection with set 2:", set1)
