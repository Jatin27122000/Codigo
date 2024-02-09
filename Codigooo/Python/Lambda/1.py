'''Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
also create a lambda function that multiplies argument x with argument y and prints the result.
Sample Output:
25
48'''
i = lambda a: a + 15
print(i(10))

r = lambda x, y: x * y
print(r(12,4))