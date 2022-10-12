with open('goats.txt') as input, open('answer.txt', 'w', encoding='utf-8') as answer:
    color_goats, total = {}, 0

    for line in input:
        if line not in ('COLOURS\n', 'GOATS\n'):
            color_goats[line] = color_goats.get(line, -1) + 1
            total += 1

    print(*sorted([x[0] for x in color_goats.items() if x[1] * 100 / total > 7]), sep='')

