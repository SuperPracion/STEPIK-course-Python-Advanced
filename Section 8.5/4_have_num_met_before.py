set_num = set()
mass_num = [int(num) for num in input().split()]

for num in mass_num:
    if num in set_num:
        print('YES')
    else:
        print('NO')
        set_num.add(num)