def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(f'{num:<3d}', end='')
        print()


n = int(input())

matrix = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
        matrix[0][i], matrix[n - 1][i] = matrix[n - 1][i], matrix[0][i]
print_matrix(matrix)