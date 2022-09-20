# for _ in range(int(input())):
#     print(len(set(input().lower())))

n = int(input())
set_strings = [set(input().lower()) for _ in range(n)]

for string in set_strings:
    print(len(string))