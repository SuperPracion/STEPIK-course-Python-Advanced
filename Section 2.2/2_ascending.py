mass_nums = [int(num) for num in input().split()]
num_bigger_that_last = 0

for i in range(1, len(mass_nums)):
    if mass_nums[i - 1] < mass_nums[i]:
        num_bigger_that_last += 1

print(num_bigger_that_last)