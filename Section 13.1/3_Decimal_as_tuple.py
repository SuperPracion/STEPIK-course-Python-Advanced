from decimal import *
nums = Decimal(str(abs(Decimal(input())))[::-1]).as_tuple().digits

print(nums)
