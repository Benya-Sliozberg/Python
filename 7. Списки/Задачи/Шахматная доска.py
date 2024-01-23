def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(f'{num:<3d}', end='')
        print()



n = int(input())
m = int(input())
matrix = [[0 if (i + j) % 2 == 0 else 1  for i in range(m)] for j in range(n)]
print_matrix(matrix)