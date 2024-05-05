
def square(x):
    return x ** 2

list = [1, 2, 3, 4]
result_dict = {x: square(x) for x in list}

print(result_dict)
