n, m = [int(num) for num in input().split()]
matrix = []

for i in range(n):
    matrix = ['.' if (i + j) % 2 == 0 else '*' for j in range(m)]
    print(*matrix[i])
