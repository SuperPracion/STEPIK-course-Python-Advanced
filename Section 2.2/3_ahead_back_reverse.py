mass_nums = [int(num) for num in input().split()]

for i in range(1, len(mass_nums), 2):
    mass_nums[i], mass_nums[i - 1] = mass_nums[i - 1], mass_nums[i]

print(*mass_nums, sep=' ')