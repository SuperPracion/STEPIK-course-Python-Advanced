file = open('nums.txt', 'rt', encoding='utf-8')
conternt = map(int, file.read().split())

print(sum(conternt))

file.close()