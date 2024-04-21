
tuple = ('a', 1, 'b', 2)
result = {tuple[i]: tuple[i + 1] for i in range(0, len(tuple), 2)}

print(result)

