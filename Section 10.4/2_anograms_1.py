f_dict = {}
for char in input():
    f_dict[char] = f_dict.get(char, 0) + 1

s_dict = {}
for char in input():
    s_dict[char] = s_dict.get(char, 0) + 1

if f_dict == s_dict:
    print('YES')
else:
    print('NO')

