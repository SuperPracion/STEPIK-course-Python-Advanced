def eveluate(coefficients, x):
    nums = [int(num) for num in coefficients.split()][::-1]
    return sum(map(lambda y: nums[y] * (x ** y), list(range(len(nums)))[::-1]))


print(eveluate(input(), int(input())))