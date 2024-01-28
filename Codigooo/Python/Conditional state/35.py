#Write a Python program that checks whether a string represents an integer or not.
#Expected Output:
#Input a string: Python                                                  
#The string is not an integer. 

x=input("Input a String ")
for y in x:
    if y.isdigit():
        
        print("The string is integer.")
        break
    else:
        print("The string is not an integer.") 
        break 
    
