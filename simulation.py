from random import *

list_months = {'Май': 31, 'Июнь': 30, 'Июль': 31, 'Август': 31, 'Сентябрь': 30, 'Октябрь': 31}
level_headache = {0: ['не болит'],
                  1: ['напряжение'],
                  2: ['беспокоят покалывания'],
                  3: ['головная боль'],
                  4: ['сильная головная боль'],
                  5: ['сильная головная боль, потеря дееспособности']}

duration = [minute for minute in range(5, 200)]

for month, len_month in list_months.items():
    headaches_per_month = randint(5, 18)
    days_headaches = sorted(set([randint(1, len_month) for _ in range(headaches_per_month)]))

    print(f'  {month}  '.center(80, '-'))

    for day in days_headaches:
        print(f'| {day}'.ljust(4, ' '), '|', end='')
        print(''.join(level_headache[randint(1, 5)]).ljust(50, ' '), end='')
        print('|', end='')
        print(f'{randint(0, 3)} часов'.rjust(10, ' '), end='')
        print(f'{randint(5, 60)} минут'.rjust(9, ' '), end='')
        print('   |')
