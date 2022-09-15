n = int(input())
mass = [[int(num) for num in input().split()] for _ in range(n)]
total = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        total[j][i] += mass[i][j]

for i in range(n):
    for j in range(n):
        print(total[i][j])
