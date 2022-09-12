n = int(input())
matrix = []
flag_symmetric = True

for _ in range(n):
    matrix.append([int(num) for num in input().split()])


for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag_symmetric = False
            break

print('YES' if flag_symmetric else 'NO')