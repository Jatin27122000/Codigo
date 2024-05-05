''' Write a Python program to find the first non-repeated element in a list.'''

def first_non_repeated_element(lst):
    count_dict = {}
    for elem in lst:
        count_dict[elem] = count_dict.get(elem, 0) + 1

    for elem in lst:
        if count_dict[elem] == 1:
            return elem

    return None

my_list = [1, 2, 3, 2, 1, 4, 5, 4, 6]
print(first_non_repeated_element(my_list)) 
