from functools import reduce

ip_addresses = sorted([input() for _ in range(int(input()))])
# for i in ip_addresses:
#     print(i.split('.')[::-1][0])
# print(*sorted(ip_addresses, key=lambda x: reduce(lambda y: int(x.split('.')[::-1][y]) * 255**y, list(range(4)), 1)))

print(*sorted(ip_addresses, key=lambda x: sum(int(x.split('.')[::-1][y]) * 255**y for y in range(4))), sep='\n')