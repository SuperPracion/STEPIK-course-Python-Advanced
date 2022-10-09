in_str = sorted([input() for _ in range(int(input()))])
# for i in in_str:
#     print(sum(ord(j) - 65 for j in list(i.upper())))
print(*sorted(in_str, key=lambda x: sum(ord(j) - 65 for j in list(x.upper()))), sep='\n')