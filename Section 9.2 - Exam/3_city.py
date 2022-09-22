mass_city = [input() for _ in range(int(input()) + 1)]

print('OK' if len(mass_city) == len(set(mass_city)) else 'REPEAT')