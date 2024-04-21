def reverse_string(my_string):
    if len(my_string)%4 == 0:
        return ''.join(reversed(my_string))
    else:
        return my_string

my_string = input("enter a string ")
print(reverse_string(my_string))