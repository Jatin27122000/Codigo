#Write a Python program that accepts a string and calculates the number of digits and letters.
#Sample Data : Python 3.2
#Expected Output :
#Letters 6
#Digits 2

x=input("Enter String")
d=0
l=0

for y in x:
    if y.isdigit():
        d=d+1
        
    elif y.isalpha():
        l=l+1 
            

print("Digit :", d)
print("Letter:",l) 