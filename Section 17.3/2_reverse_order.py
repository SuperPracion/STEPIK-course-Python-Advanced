with open('data.txt', 'r', encoding='utf-8') as file:
    print(*file.readlines()[::-1], sep='')