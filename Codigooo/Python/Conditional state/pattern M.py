for row in range(7):
    for column in range(5):
        if column==0 or column == 4 or (row==2 and column!=2)or row==3 and column==2:
            print("*",end=" ")
        else:
            print(end="  ")

    
    print( )