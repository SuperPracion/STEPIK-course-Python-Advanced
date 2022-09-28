from random import *
lottery_nums = set()

while len(lottery_nums) != 7:
    lottery_nums.add(randint(1, 49))

print(*sorted(lottery_nums))