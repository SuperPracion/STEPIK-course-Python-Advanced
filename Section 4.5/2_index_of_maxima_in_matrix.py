n, m = int(input()), int(input())
matrix = []

for _ in range(n):
    matrix.append([int(num) for num in input().split()])

print(matrix)

maxima = [0, 0]

for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[maxima[0]][maxima[1]]:
            maxima[0], maxima[1] = i, j

print(maxima[0], maxima[1])