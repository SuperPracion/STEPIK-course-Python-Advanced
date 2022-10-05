def sort_by_sum_nums(pair):
    return sum([int(num) for num in str(pair)]), pair

nums = [int(num) for num in input().split()]
print(*sorted(nums, key=sort_by_sum_nums))