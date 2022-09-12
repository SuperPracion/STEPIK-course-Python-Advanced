n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(num) for num in input().split()])

for i in range(n):
        matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')