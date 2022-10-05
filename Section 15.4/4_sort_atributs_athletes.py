def name(pair):
    return pair[0]

def age(pair):
    return pair[1]

def height(pair):
    return pair[2]

def weight(pair):
    return pair[3]

sort_params = {'1': name, '2': age, '3': height, '4': weight}

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
athletes = sorted(athletes, key=sort_params[input()])

for athlet in athletes:
    print(*athlet, sep=' ')
