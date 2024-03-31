# Write a Python program to print a list of space-separated elements.
num = [1, 2, 3, 4]
new_list = ['emp{0}'.format(i) for i in num]
print(new_list)