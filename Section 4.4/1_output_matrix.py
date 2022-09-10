matrix = []
n, m = int(input()), int(input())

for _ in range(n):
    temp = [input() for _ in range(m)]
    matrix.append(temp)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

# n, m = int(input()), int(input())
# matrix = [input() for _ in range(n * m)]
#
# for index in range(n * m):
#     if index % m == 0:
#         print()
#     print(matrix[index])
