def mean(*args):
    nums = [num for num in args if type(num) in (int, float)]
    return  sum(nums) / len(nums) if nums else 0.0

print(mean(1.5, True, ['stepik'], 'beegeek', 2.5))