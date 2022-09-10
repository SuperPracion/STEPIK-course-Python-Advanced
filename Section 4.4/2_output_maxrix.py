n, m = int(input()), int(input())
matrix = []

for _ in range(n):
    temp = [input() for _ in range(m)]
    matrix.append(temp)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

for i in range(n):
    for j in range(m):
        print(matrix[j][i], end=' ')
    print()