def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted_row = ' '.join(["{:d}".format(cell) for cell in row])
        print(formatted_row)