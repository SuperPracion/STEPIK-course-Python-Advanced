import re

with open('nums.txt', 'r', encoding='utf-8') as file:
    total = 0
    for line in file.readlines():
        total += sum(map(int, re.findall('\d+', line)))

    print(total)

# print('bhjip456qwerty'.strip())