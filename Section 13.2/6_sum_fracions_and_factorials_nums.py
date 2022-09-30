from math import factorial
from fractions import Fraction

n = int(input())
sum = 0

for num in range(1, n + 1):
    sum += 1 / Fraction(factorial(num))

print(sum)