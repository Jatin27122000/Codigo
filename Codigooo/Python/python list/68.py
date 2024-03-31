'''Write a Python program to extend a list without appending.
Sample data: [10, 20, 30]
[40, 50, 60]
Expected output : [40, 50, 60, 10, 20, 30]'''

x = [10, 20, 30]
y = [40, 50, 60]
x[:0] =y
print(x)