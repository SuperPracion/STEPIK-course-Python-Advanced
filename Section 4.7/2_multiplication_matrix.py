n1, m1 = [int(num) for num in input().split()]
matrix1 = [[int(num) for num in input().split()] for _ in range(n1)]

input()

n2, m2 = [int(num) for num in input().split()]
matrix2 = [[int(num) for num in input().split()] for _ in range(n2)]

n3, m3 = max(n1, n2), max(m1, m2)
total_matrix = [[0 for _ in range(m3)] for _ in range(n3)]

for i in range(n3):
    for j in range(m3):
        for x in range(m1):
            total_matrix[i][j] += matrix1[i][x] * matrix2[x][j]

for i in range(n3):
    for j in range(m3):
        print(total_matrix[i][j], end='')
    print()
