import random

file = open('lines.txt', 'rt', encoding='utf-8')
content = file.readlines()

print(random.choice(content))

file.close()