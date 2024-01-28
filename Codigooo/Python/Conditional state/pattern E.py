for row in range(0,7):
    
    for column in range(0,5):
        if column==0 or row==0 or (row==3 and column!=3)or row==6:
            print("*",end="")  
        else:
            print(end="")


    print()

    