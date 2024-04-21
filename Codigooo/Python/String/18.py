def first_three(my_string):
    if len(my_string) > 2:
        return my_string[:3]
    else:
        return my_string
print(first_three('ipy'))
print(first_three('python'))