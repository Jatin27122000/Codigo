import string
my_string = input("enter a string ")

# solution 1
alphabet = 'abcdefghijklmnopqrstuvwxyz'
counter = 0
for letter in alphabet:
    if letter in my_string.lower():
        counter += 1
    else:
        break
if counter == 26:
    print('the string contains all the letters of the alphabet')
else:
    print('the string DOES NOT contain all the letters of the alphabet')