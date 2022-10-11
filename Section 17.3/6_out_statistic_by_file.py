with open('file.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    print('Input file contains:')
    print(sum(map(str.isalpha, text)), 'letters')
    print(len(text.split()), 'words')
    print(text.count('\n') + 1, 'lines')
