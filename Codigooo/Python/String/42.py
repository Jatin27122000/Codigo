my_string = input("enter a string ")
my_dict = {}
for letter in my_string:
    if letter in my_dict:
        my_dict[letter] += 1
    else:
        my_dict[letter] = 1
for key, value in my_dict.items():
    print(key, value)