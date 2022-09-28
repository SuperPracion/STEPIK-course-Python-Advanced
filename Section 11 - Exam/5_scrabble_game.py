game_points = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'], 2: ['D', 'G'], 3: ['B', 'C', 'M', 'P'],
               4: ['F', 'H', 'V', 'W', 'Y'], 5: ['K'], 8: ['J', 'X'], 10: ['Q', 'Z']}

count = 0
for symbol in tuple(input()):
    for key in game_points.keys():
        if symbol in game_points[key]:
            count += key

print(count)