n = int(input())
mass = []

for len in range(1, n + 1):
    mass.append([num for num in range(1, len + 1)])

print(*mass, sep='\n')

# n = int(input())
#
# for len in range(1, n + 1):
#     print([num for num in range(1, len + 1)])