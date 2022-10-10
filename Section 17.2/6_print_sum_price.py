file = open('prices.txt', 'rt', encoding='utf-8')
content = map(str.split, file)
# content = list(map(lambda x: int(x.split()[2]), file.readlines()))

print(sum(map(lambda x: int(x[1]) * int(x[2]), content)))

file.close()