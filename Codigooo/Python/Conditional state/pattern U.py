for row in range(7):
    for column in range(5):
        if row==6 and column != 0 and column !=4 or ((column == 0 or column == 4) and row != 6) :
            print("*",end="")
        else:
            print(end=" ")

    
    print( )