for row in range(7):
    for column in range(5):
        if (column == 0 and row !=0  and row!=3)  or (row==0 and  column!=0 ) or (column == 4 and row!=0 and row!=6  )or (row==6 and column!=0 and column!=4) or (row == 0 or row ==3 )and (column > 0 and column < 4):  
            print("*",end=" ")
        else:
            print(end="  ")

    
    print( )