'''Write a Python function that finds all the permutations of the members of a list.'''

def permutations(lst):
    if len(lst) == 0:
        return [[]]  

    result = []
    for i in range(len(lst)):
        current = lst[i]
        remaining = lst[:i] + lst[i+1:]

        for p in permutations(remaining):
            result.append([current] + p)

    return result

my_list = [1, 2, 3]
print(permutations(my_list))
