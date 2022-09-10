n = int(input())
matrix = []

for _ in range(n):
    temp = [int(num) for num in input().split()]
    average_temp = sum(temp) / n

    print(sum([1 for num in temp if num > average_temp]))

    matrix.append(temp)

