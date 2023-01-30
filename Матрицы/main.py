def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(f'{num:<3d}', end='')
        print()


rows = 10
cols = 15
matrix = [[0 for i in range(cols)] for j in range(rows)]

print_matrix(matrix)
