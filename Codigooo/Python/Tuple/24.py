my_list = [1, 2, 3, (4,), 5, 6]

counter = 0
for i in my_list:
    if not isinstance(i, tuple):
        counter += 1
    else:
        break
print(counter)

