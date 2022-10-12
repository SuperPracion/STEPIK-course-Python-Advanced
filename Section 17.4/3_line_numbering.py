with open('output.txt', 'w', encoding='utf-8') as output, open('input.txt', 'rt', encoding='utf-8') as input:
    line_num = 1
    for line in input:
        output.write(f'{line_num}) {line}')
        line_num += 1