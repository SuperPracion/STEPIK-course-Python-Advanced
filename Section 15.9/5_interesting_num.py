a = int(input())
b = int(input())

# print([map(lambda x: all(0 not in tuple(x) and all(map(lambda y: x % y == 0, tuple(x)))), list(range(a, b + 1)))])

# for x in range(1, 26):
#     if all(map(lambda y: y != '0' and x % int(y) == 0, tuple(str(x)))):
#         print(x)

# print(*list(filter(lambda z: z != '', map(lambda x: x if all(map(lambda y: int(y) and x % int(y) == 0, tuple(str(x)))) else '', list(range(a, b + 1))))))

print(*list(filter(lambda x: all(map(lambda y: int(y) and x % int(y) == 0, tuple(str(x)))), list(range(a, b + 1)))), sep=' ')