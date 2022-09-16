n = int(input())
mass = [['.'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i == j) or (j == n - i - 1) or (i == n // 2) or (j == n // 2):
            mass[i][j] = '*'

for list in mass:
    print(*list)