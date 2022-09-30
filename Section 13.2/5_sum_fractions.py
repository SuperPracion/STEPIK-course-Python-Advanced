from fractions import Fraction
sum = 0

n = int(input())
for num in range(1, n + 1):
    sum += 1 / Fraction(num ** 2)

print(sum)