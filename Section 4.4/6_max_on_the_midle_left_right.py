# n = int(input())
# matrix = []
#
# for _ in range(n):
#     matrix.append([int(num) for num in input().split()])
#
# print(matrix)
#
# maxima = matrix[0][0]
#
# for i in range(n):
#     for j in range(n):
#         if (i > j and i < n - 1 - j) or (i > j and i > n - 1 - j) and matrix[i][j] > maxima:
#             maxima = matrix[i][j]
#
# print(maxima)


def fill_matrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append([int(num) for num in input().split()])

    return matrix


def get_max_on_the_left_right(matrix, n):
    maxima = matrix[0][0]

    for i in range(n):
        for j in range(n):
            if ((j <= i <= n - 1 - j) or (j >= i >= n - 1 - j)) and matrix[i][j] > maxima:
                maxima = matrix[i][j]

    return maxima


n = int(input())
matrix = fill_matrix(n)
print(get_max_on_the_left_right(matrix, n))
