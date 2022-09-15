mass = input().split()
total = []
n = int(input())

for i in range(n):
    total.append([mass[j] for j in range(i, len(mass), n)])

print(total)