n, m = [int(num) for num in input().split()]
matrix = [[0 for _ in range(m)] for _ in range(n)]

count = 0
for q in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                count += 1
                matrix[i][j] = count

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()