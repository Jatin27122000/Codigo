
str1 = 'abc'
str2 = 'string'


if len(str1) >= 3:
    
    if str1.endswith('ing'):
        
        result1 = str1 + 'ly'
    else:
        # Otherwise, add 'ing' at the end
        result1 = str1 + 'ing'
else:
    # If the length is less than 3, leave it unchanged
    result1 = str1


print("Result for 'abc':", result1)

# Check the second string
if len(str2) >= 3:
    # Check if the string already ends with 'ing'
    if str2.endswith('ing'):
        # If yes, add 'ly' instead
        result2 = str2 + 'ly'
    else:
       
        result2 = str2 + 'ing'
else:
   
    result2 = str2


print("Result for 'string':", result2)
