n = int(input())
mass = [[int(num) for num in input().split()] for _ in range(n)]

maxima = mass[0][0]

for i in range(n):
    for j in range(n):
        if ((i <= j and i >= n - 1 - j) or (i >= j and i >= n - 1 - j)) and mass[i][j] > maxima:
            maxima = mass[i][j]

print(maxima)