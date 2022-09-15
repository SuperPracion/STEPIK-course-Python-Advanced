n = int(input())
mass = [[int(num) for num in input().split()] for _ in range(n)]
need_nums = [i + 1 for i in range(n)]
flag_latin_square = True

for i in range(n):
    hor_need_nums = need_nums.copy()
    ver_need_nums = need_nums.copy()
    for j in range(n):
        if mass[i][j] in hor_need_nums and mass[j][i] in ver_need_nums:
            del hor_need_nums[hor_need_nums.index(mass[i][j])]
            del ver_need_nums[ver_need_nums.index(mass[j][i])]
        else:
            flag_latin_square = False

print('YES' if flag_latin_square else 'NO')
