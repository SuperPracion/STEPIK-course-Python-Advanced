def degress_matrix(total_matrix_def, matrix_def, n):
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for x in range(n):
                new_matrix[i][j] += total_matrix_def[x][j] * matrix_def[i][x]

    return new_matrix


n = int(input())
matrix = [[int(num) for num in input().split()] for num in range(n)]
degree = int(input()) - 1

total_matrix = matrix

for _ in range(degree):
    total_matrix = degress_matrix(total_matrix, matrix, n)

for i in range(n):
    for j in range(n):
        print(total_matrix[i][j], end=' ')
    print()