n = int(input())
mass = [[int(num) for num in input().split()] for _ in range(n)]
flag_symmetry = True

for i in range(n):
    for j in range(n):
        if not j == n - i - 1:
            if mass[i][j] != mass[n - 1 - j][n - 1 - i]:
                flag_symmetry = False
                break

print('YES' if flag_symmetry else 'NO')