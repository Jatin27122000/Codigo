my_string = input("enter a text ")

vowels = 'aeiouy'
my_string = my_string.lower()
my_list = [(x, my_string.count(x)) for x in my_string if x in vowels]
print(set(my_list))