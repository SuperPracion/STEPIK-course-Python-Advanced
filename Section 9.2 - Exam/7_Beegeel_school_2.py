m, n = int(input()), int(input())

f_set = set(input() for _ in range(m))
s_set = set(input() for _ in range(n))

print(len(f_set ^ s_set))