from random import *

bingo_ticket = sample(list(range(1, 76)), 25)
bingo_ticket[12] = 0

for i in range(0, 21, 5):
    print(*bingo_ticket[i: i + 5])
