'''Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''

a = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

for x in a:
    del(a[0])
    del(a[4])
    del(a[5]) 
    print(a)
    
     
        
        