def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(f'{num:<3d}', end='')
        print()


n, m = list(map(int, input().split()))

matrix = [list(map(int, input().split())) for j in range(n)]
a, b = list(map(int, input().split()))
for i in range(n):
    matrix[i][a],matrix[i][b] = matrix[i][b],matrix[i][a]
print_matrix(matrix)