def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(f'{num:<3d}', end='')
        print()


n, m = list(map(int, input().split()))

matrix = [list(map(int, input().split())) for j in range(n)]
imax = 0
jmax = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[imax][jmax]:
            imax = i
            jmax = j
print(imax, jmax)