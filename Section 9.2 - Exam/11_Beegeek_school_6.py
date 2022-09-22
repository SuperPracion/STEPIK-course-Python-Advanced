m = int(input()) - 1
last_names = set(input() for _ in range(int(input())))

for _ in range(m):
    last_names &= set(input() for _ in range(int(input())))

print(*sorted(last_names))