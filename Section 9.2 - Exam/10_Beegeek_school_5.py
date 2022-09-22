m, n = int(input()), int(input())
last_names_set = set()

for _ in range(n + m):
    last_name = input()

    if last_name not in last_names_set:
        last_names_set.add(last_name)
    else:
        last_names_set.discard(last_name)

print(len(last_names_set) if last_names_set else 'NO')