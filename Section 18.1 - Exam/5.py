with open(input(), 'rt', encoding='utf-8') as file:
    content = file.readlines()
    print(*content[-10:], sep='')