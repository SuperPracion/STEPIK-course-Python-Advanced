n = int(input())
tribonacci = [1, 1, 1]

for num in range(2, n):
    tribonacci.append(sum(tribonacci[-3:]))

print(*tribonacci[:n])