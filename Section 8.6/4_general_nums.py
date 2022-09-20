n = int(input())
mass_sets = set(input())

for _ in range(n - 1):
    mass_sets = mass_sets & set(input())

print(*sorted(mass_sets))