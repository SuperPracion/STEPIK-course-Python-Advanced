n = int(input())
slang_dict = {}

for _ in range(n):
    key, value = input().split(': ')
    slang_dict[key.lower()] = value

m = int(input())
for _ in range(m):
    print(slang_dict.get(input().lower(), 'Не найдено'))