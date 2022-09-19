mass = set([int(num) for num in input() + input()])

print('YES' if sum(mass) == 45 and len(mass) == 10 else 'NO')