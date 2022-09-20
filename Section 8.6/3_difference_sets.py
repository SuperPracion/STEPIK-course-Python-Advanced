mass1 = set(int(num) for num in input().split())
mass2 = set(int(num) for num in input().split())

print(*sorted(mass1 - mass2))