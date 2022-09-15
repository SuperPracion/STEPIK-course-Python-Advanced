n = int(input())
mass = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        mass[i][j] = abs(j - i)

for i in range(n):
    for j in range(n):
        print(mass[i][j], end=' ')
    print()