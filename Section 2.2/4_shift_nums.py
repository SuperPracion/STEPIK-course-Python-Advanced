mass_nums = [int(num) for num in input().split()]

print(mass_nums[-1], *mass_nums[:-1], sep=' ')