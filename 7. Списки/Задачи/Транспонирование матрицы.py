def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(f'{num:<3d}', end='')
        print()


n, m = list(map(int, input().split()))

matrix = [list(map(int, input().split())) for j in range(n)]
matrix_t = []
for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(matrix[j][i])
    matrix_t.append(tmp)
print_matrix(matrix_t)