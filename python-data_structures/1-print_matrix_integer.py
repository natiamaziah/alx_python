def print_matrix_integer(matrix=[[]]):
   matrix = []
   for row in matrix:
        for elem in row:
            print("{:d}".format(elem),end=" ")
        print()
           
print_matrix_integer()