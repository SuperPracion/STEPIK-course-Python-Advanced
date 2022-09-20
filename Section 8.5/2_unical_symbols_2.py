n = int(input())
set_string = set()

for _ in range(n):
    for symbol in set(input().lower()):
        set_string.add(symbol)

print(len(set_string))