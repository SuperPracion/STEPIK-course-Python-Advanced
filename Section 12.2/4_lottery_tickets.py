from random import *

lottery_tickets = set()

while len(lottery_tickets) != 100:
    lottery_tickets.add(randint(1000000, 9999999))

print(*lottery_tickets, sep='\n')