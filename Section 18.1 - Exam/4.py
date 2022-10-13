with open('words.txt', 'rt', encoding='utf-8') as file:
    content = file.read().split()
    max_len = len(max(content, key=len))

    for word in content:
        if len(word) == max_len:
            print(word)