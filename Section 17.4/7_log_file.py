def hours_in_minutes(hourse):
    res = [int(i) for i in hourse.split(':')]
    return res[0]*60 + res[1]

with open('logfile.txt', 'rt', encoding='utf-8') as input, open('output.txt', 'w', encoding='utf-8') as output:
    for line in input:
        name, data_in, data_out = line.split(',')
        if hours_in_minutes(data_out) - hours_in_minutes(data_in) >= 60:
            print(name, file=output)