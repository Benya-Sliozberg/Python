def print_matrix(matrix):
    for row in matrix:
        for num in row:
            if num == 9:
                print(f'*', end='  ')
            elif num == 0:
                print(f'.', end='  ')
            else:
                print(f'{num:<3d}', end='')
        print()


n, m, k = list(map(int, input().split()))
matrix = [[0 for i in range(m)] for j in range(n)]
for _ in range(k):
    x, y = list(map(int, input().split()))
    matrix[x-1][y-1] = 9
for i in range(n):
    for j in range(m):
        count = 0
        if i > 0 and matrix[i - 1][j] == 9:
            count += 1
        if i < n - 1 and matrix[i + 1][j] == 9:
            count += 1
        if j < m - 1 and matrix[i][j + 1] == 9:
            count += 1
        if j > 0 and matrix[i][j - 1] == 9:
            count += 1
        if i > 0 and j < m - 1 and matrix[i - 1][j + 1] == 9:
            count += 1
        if i < n - 1 and j > 0 and matrix[i - 1][j - 1] == 9:
            count += 1
        if i < n - 1 and j < m - 1 and matrix[i + 1][j + 1] == 9:
            count += 1
        if i < n - 1 and j > 0 and matrix[i + 1][j - 1] == 9:
            count += 1
        if matrix[i][j] == 0:
            matrix[i][j] = count
print_matrix(matrix)

