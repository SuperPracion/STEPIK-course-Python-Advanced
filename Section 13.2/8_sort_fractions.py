from fractions import Fraction

f_set = set()
for i in range(int(input()), 1, -1):
    for j in range(1, i):
        f_set.add(Fraction(j, i))

print(*sorted(f_set), sep='\n')