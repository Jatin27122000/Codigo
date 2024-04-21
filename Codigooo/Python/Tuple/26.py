
tuples = [(4, 3, 2, 2, -1, 18), (2, 4, 8, 8, 3, 2, 9)]


for ntuple in tuples:
    product = 1
    for num in ntuple:
        product *= num
    print("Original Tuple:")
    print(ntuple)
    print("Product - multiplying all the numbers of the said tuple:", product)
