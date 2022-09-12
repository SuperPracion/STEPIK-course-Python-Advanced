# n, m = int(input()), int(input())
# matrix = []
#
# for _ in range(n):
#     matrix.append([int(num) for num in input().split()])
#
# split_a, split_b = [int(num) for num in input().split()]
#
# for i in range(n):
#     matrix[i][split_a], matrix[i][split_b] = matrix[i][split_b], matrix[i][split_a]
#
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end='')
#     print()


def filling_matrix(n, m):
    matrix = []

    for _ in range(n):
        matrix.append([int(num) for num in input().split()])

    return matrix


def split_columns(colum_a, colum_b, matrix):
    for i in range(len(matrix)):
        matrix[i][colum_a], matrix[i][colum_b] = matrix[i][colum_b], matrix[i][colum_a]

    return matrix


n, m = int(input()), int(input())
matrix = filling_matrix(n, m)

a, b = [int(num) for num in input().split()]
matrix = split_columns(a, b, matrix)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end='')
    print()
