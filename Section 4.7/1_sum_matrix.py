n, m = [int(num) for num in input().split()]

matrxi_1 = [[int(num) for num in input().split()] for _ in range(n)]
input()
matrxi_2 = [[int(num) for num in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(matrxi_1[i][j] + matrxi_2[i][j], end='')
    print()