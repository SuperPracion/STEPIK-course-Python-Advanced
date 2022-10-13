with open('forbidden_words.txt', 'rt', encoding='utf-8') as f1, open('data.txt', 'rt', encoding='utf-8') as f2:
    bad_words = f1.read().split()
    content = f2.read()
    replace_content = content.lower()

    for word in bad_words:
        replace_content = replace_content.replace(word.lower(), '*'*len(word))

    for word in range(len(replace_content)):
        if replace_content[word] != '*':
            print(content[word], end='')
        else:
            print('*', end='')
