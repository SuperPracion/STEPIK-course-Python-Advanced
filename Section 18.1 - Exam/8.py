with open(input(), 'rt', encoding='utf-8') as file:
    count_miss_def = 0
    content = ['\n'] + file.readlines()

    for i in range(1, len(content)):
        if 'def' in content[i] and '#' not in content[i - 1]:
            print(content[i][4:content[i].find('(')], end='\n')
            count_miss_def += 1

    if not count_miss_def:
        print('Best Programming Team')