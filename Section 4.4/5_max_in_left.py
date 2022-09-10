n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(num) for num in input().split()])

maxima = matrix[0][0]

for i in range(n):
    for j in range(n):
        if i >= j and matrix[i][j] > maxima:
            maxima = matrix[i][j]

print(maxima)

# def get_maxima_on_the_left(matrix):
#     maxima = matrix[0][0]
#
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if i >= j and matrix[i][j] > maxima:
#                 maxima = matrix[i][j]
#
#     return maxima
#
#
# def filling_matrix(rows, cols):
#     matrix = []
#
#     for _ in range(rows):
#         matrix.append([int(num) for num in input().split()])
#
#     return matrix
#
#
# n = int(input())
# matrix = filling_matrix(n, n)
# print(get_maxima_on_the_left(matrix))
