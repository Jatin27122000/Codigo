for row in range(7):
    for column in range(5):
        if column==0 or (row==0 and column!=4) or (row==3 and column!=4)or (column==4 and row!=0 and row!=3 and row!=4 and row!=5 ) or (row==4 and column==2) or (row==5 and column==3) :
            print("*",end=" ")
        else:
            print(end="  ")

    
    print( )