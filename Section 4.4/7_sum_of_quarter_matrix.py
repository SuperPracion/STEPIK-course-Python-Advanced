n = int(input())
matrix = []
list_quarter = [0, 0, 0, 0]

for _ in range(n):
    matrix.append([int(num) for num in input().split()])

for i in range(n):
    for j in range(n):
        num = matrix[i][j]

        if i < j:
            if i < n - 1 - j:
                list_quarter[0] += num
            elif i > n - 1 - j:
                list_quarter[1] += num

        if i > j:
            if i < n - 1 - j:
                list_quarter[3] += num
            elif i > n - 1 - j:
                list_quarter[2] += num

print(f'Верхняя четверть: {list_quarter[0]}')
print(f'Правая четверть: {list_quarter[1]}')
print(f'Нижняя четверть: {list_quarter[2]}')
print(f'Левая четверть: {list_quarter[3]}')