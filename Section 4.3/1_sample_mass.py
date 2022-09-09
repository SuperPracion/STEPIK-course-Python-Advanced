n = int(input())
mass = []

for _ in range(n):
    mass.append([num for num in range(1, n + 1)])

print(*mass, sep='\n')

# n = int(input())
#
# for _ in range(n):
#     print([num for num in range(1, n + 1)])