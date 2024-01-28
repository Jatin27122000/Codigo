for row in range(5):
    
    for column in range(7):
        if (((column == 0 or column == 4) and row != 0) or ((row == 0 or row ==3 )and (column > 0 and column < 4))):
            print("*",end="")  
        else:
            print(end=" ")


     
   


    print()