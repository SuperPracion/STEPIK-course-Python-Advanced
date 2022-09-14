n, m = [int(num) for num in input().split()]
matrix = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = (m * i) + j + 1
    if i % 2 == 1:
        matrix[i].reverse()

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()