for row in range(0,7):
    
    for column in range(0,7):
        if row==0 or row==6 or row+column==6:
            print("*",end="")  
        else:
            print(end=" ")


    print()