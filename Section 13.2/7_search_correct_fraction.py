from fractions import Fraction
from math import gcd
n = int(input())
num = 0

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        if gcd(j, i) == 1 and i + j == n and i > j:
            num = Fraction(j, i)

print(num)