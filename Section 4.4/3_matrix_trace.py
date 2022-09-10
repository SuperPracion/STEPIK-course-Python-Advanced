n = int(input())
matrix = []
sum_main_matrix_line = 0

for i in range(n):
    matrix.append([int(num) for num in input().split()])
    sum_main_matrix_line += matrix[i][i]

print(sum_main_matrix_line)