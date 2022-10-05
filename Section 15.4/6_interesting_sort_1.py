def sort_by_sum(pair):
    return sum([int(num) for num in pair])

nums = [num for num in input().split()]
nums = sorted(nums, key=sort_by_sum)