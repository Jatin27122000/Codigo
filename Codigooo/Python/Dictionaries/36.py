list_one = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
list_two = [1, 2, 2, 3]

my_dict = {k: v for (k, v) in zip(list_one, list_two)}
print(my_dict)