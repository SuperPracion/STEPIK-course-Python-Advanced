n = int(input())
mass = [['.' for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i == j) or (j == n - i - 1) or (i == n // 2) or (j == n // 2):
            mass[i][j] = '*'

for i in range(n):
    for j in range(n):
        print(mass[i][j], end=' ')
    print()