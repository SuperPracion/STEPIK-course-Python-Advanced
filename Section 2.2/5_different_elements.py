mass_num = [int(num) for num in input().split()]
count_diff_num = 1

for i in range(1, len(mass_num)):
    if mass_num[i - 1] != mass_num[i]:
        count_diff_num += 1

print(count_diff_num)

