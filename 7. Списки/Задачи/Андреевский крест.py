def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(f'{num:<3d}', end='')
        print()



n = int(input())
matrix = [[1 if i == j or i == n - j - 1 else 0 for i in range(n)] for j in range(n)]
print_matrix(matrix)