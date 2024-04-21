def to_upper(my_string):
    counter = 0
    for i in my_string[:4]:
        if i.isupper():
            counter += 1
    if counter > 1:
        return my_string.upper()
    else:
        return my_string

my_string = input("enter a string ")
print(to_upper(my_string))