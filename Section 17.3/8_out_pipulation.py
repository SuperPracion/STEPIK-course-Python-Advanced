with open('population.txt', 'r', encoding='utf-8') as population:
    for line in population.readlines():
        country, pop = line.split('\t')

        if country[0] == 'G' and int(pop) > 500000:
            print(country)