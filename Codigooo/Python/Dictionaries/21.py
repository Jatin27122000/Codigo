from itertools import product

data = {'1': ['a', 'b'], '2': ['c', 'd']}
combinations = [''.join(comb) for comb in product(*data.values())]

for combination in combinations:
    print(combination)
