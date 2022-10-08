abscissas = [float(i) for i in input().split()]
ordinates = [float(i) for i in input().split()]
applicates = [float(i) for i in input().split()]

print(all([x**2 + y**2 + z**2 < 4 for x, y, z in zip(abscissas, ordinates, applicates)]))
