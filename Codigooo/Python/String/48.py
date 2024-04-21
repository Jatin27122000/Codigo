my_string = '32.054,23'
print(my_string)
swap = str.maketrans(',.', '.,')
new_string = my_string.translate(swap)
print(new_string)