def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(f'{num:<3d}', end='')
        print()


def get_value(i, j):
    if i == j or i == n - j - 1:
        return 0
    if i > j and i < n - j - 1:
        return 1
    if i > j and i > n - j - 1:
        return 2
    if i < j and i > n - j - 1:
        return 3
    return 4


n = int(input())
matrix = [[get_value(i, j) for i in range(n)] for j in range(n)]
print_matrix(matrix)
