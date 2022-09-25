f_str = sorted([symbol for symbol in input().lower() if symbol.isalpha()])
s_str = sorted([symbol for symbol in input().lower() if symbol.isalpha()])

print(f_str, s_str)

print('YES' if f_str == s_str else 'NO')