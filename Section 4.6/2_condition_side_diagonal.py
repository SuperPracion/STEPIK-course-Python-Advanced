def get_right_num(i, j, n):
    result = -1

    if i == n - j - 1:
        result = 1
    elif i < n - j - 1:
        result = 0
    else:
        result = 2

    return result


n = int(input())
matrix = [[get_right_num(i, j, n) for j in range(n)] for i in range(n)]

for line in matrix:
    print(*line)
