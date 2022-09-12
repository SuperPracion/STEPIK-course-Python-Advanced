n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(num) for num in input().split()])

for i in range(n):
    for j in range(n):
        matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]

for i in range(n):
    print(str(matrix[i]))