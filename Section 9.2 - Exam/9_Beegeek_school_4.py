f_set_last_names = set(input().split())
s_set_last_names = set(input().split())

print(*sorted(f_set_last_names | s_set_last_names))