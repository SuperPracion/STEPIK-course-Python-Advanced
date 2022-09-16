n = int(input())
mass = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        mass[j][i], mass[i][j] = mass[i][j], mass[j][i]

for list in mass:
    print(*mass)