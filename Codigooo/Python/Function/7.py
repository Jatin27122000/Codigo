''' Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12'''



'''def fun(n):
        lower=0
        upper=0
        for i in n:
            if(i.islower()):
                lower+=1
                pass
            else:
                upper+=1
                pass
        print("The number of lowercase characters is:",lower)
        print("The number of uppercase characters is:",upper)
        
string = "The quick Brow Fox"
fun(string)'''


def fun(n):
    
    upper = 0
    lower = 0
    up="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lo="abcdefghijklmnopqrstuvwxyz"
    for i in string:
        if i in up:
            upper+=1
        elif i in lo:
            lower+=1
    print('Lower case characters = %s' %lower)
    print('Upper case characters = %s' %upper)
    
string = "The quick Brow Fox"
fun(string)