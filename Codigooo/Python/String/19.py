def get_last_part(my_string, char):
    position = my_string.rfind(char)
    return my_string[:position]
print(get_last_part('https://www.w3resource.com/python', "/"))