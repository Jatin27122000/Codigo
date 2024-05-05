'''Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.
Original Matrix:
[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
Sort the said matrix in ascending order according to the sum of its rows
[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
Original Matrix:
[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
Sort the said matrix in ascending order according to the sum of its rows
[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]'''

original_matrices = [[[1, 2, 3], [2, 4, 5], [1, 1, 1]],
                      [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]]

row_sum = lambda matrix: sum(matrix)

sort_matrix_by_row_sum = lambda matrix: sorted(matrix, key=row_sum)

for matrix in original_matrices:
    sorted_matrix = sort_matrix_by_row_sum(matrix)
    
    print("Original Matrix:")
    print(matrix)
    print("Sort the said matrix in ascending order according to the sum of its rows")
    print(sorted_matrix)
    print()
