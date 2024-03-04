def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    new_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row to store the squared values for the current row
        new_row = []

        # Iterate through each element in the current row and square it
        for element in row:
            new_row.append(element ** 2)

        # Append the new row to the new_matrix
        new_matrix.append(new_row)

    return new_matrix

# Test the function
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
