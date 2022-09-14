n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or (i + j == n - 1):
            matrix[i][j] = 1

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end='')
    print()