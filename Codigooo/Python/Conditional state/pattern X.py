for row in range(7):
    for column in range(5):
        if (((column == 1 or column == 5) and (row > 4 or row < 2)) or row == column and column > 0 and column < 6 or (column == 2 and row == 4) or (column == 4 and row == 2)):
            print("*",end=" ")
        else:
            print(end="  ")

    
    print( )