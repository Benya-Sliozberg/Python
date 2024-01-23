def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(f'{num:<3d}', end='')
        print()



n = int(input())
m = int(input())
matrix = [[i*j for i in range(m)] for j in range(n)]
print_matrix(matrix)