n, m = [int(num) for num in input().split()]
# matrix = []

matrix = [[str(j + i).ljust(3) for j in range(m)]for i in range(1, n * m + 1, m)]

# for i in range(1, n * m + 1, m):
#     matrix.append([j + i for j in range(m)])

for line in matrix:
    print(''.join(line))