in_str = input().split()
print(*sorted(in_str, key=lambda x: x.lower()), sep=' ')