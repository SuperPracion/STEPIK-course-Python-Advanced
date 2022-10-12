with open('class_scores.txt', 'rt', encoding='utf-8') as input, open('new_scores.txt', 'w', encoding='utf-8') as output:
    for line in input:
        person, point = line.split()
        print(f'{person} {(int(point) + 5)  if int(point) + 5 < 100 else 100}', file=output)