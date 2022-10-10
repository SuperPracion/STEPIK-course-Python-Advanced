file = open('numbers.txt', 'rt', encoding='utf-8')
content = [int(i) for i in file]

print(sum(content))

file.close()