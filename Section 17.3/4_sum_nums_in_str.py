with open('numbers.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        print(sum(map(int, line.split())))