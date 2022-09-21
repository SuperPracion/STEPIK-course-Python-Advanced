mass_set1 = set(input())
mass_set2 = set(input())

print('YES' if not mass_set1.isdisjoint(mass_set2) else 'NO')