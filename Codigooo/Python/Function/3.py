'''Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
'''
def mul(n):
    product=1
    for i in n:
        product*=i
    return product

n=(8, 2, 3, -1, 7)
print(mul(n))