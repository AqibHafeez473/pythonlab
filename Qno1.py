def add_matrices(matrix1, matrix2):
    # Check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same dimensions for addition."

    # Initialize an empty result matrix with the same dimensions
    result = [[0 for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

    # Add corresponding elements from the two matrices
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

# Example matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = add_matrices(matrix1, matrix2)

if isinstance(result, str):
    print(result)
else:
    print("Resultant Matrix:")
    for row in result:
        print(row)
