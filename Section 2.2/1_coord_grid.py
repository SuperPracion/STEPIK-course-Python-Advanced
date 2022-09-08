count = [0, 0, 0, 0]
coord_grid = ['Первая четверть:', 'Вторая четверть:', 'Третья четверть:', 'Четвертая четверть:']

for _ in range(int(input())):
    x, y = [int(num) for num in input().split()]

    if x > 0 and y > 0:
        count[0] += 1
    if x < 0 and y > 0:
        count[1] += 1
    if x < 0 and y < 0:
        count[2] += 1
    if x > 0 and y < 0:
        count[3] += 1

for i in range(5):
    print(coord_grid[i], count[i])
