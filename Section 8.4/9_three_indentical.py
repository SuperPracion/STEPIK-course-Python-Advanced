mass = [set(sorted(string)) for string in input().split()]

print('YES' if mass[0] == mass[1] == mass[2] else 'NO')