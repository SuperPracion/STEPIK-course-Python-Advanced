with open('lines(1).txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
    max_len_line = len(max(content, key=len))
    print(*filter(lambda x: len(x) == max_len_line, content), sep='')