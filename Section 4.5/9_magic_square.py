def filling_matrix(matrix, n):
    # заполнение
    for _ in range(n):
        matrix.append([int(num) for num in input().split()])

    return matrix


def search_duplicate(matrix, n):
    flag_dont_have_duplicate = True

    for i in range(n):
        for j in range(n):
            duplicate_num = 0
            for k in matrix:
                duplicate_num += k.count(matrix[i][j])
            if duplicate_num > 1:
                flag_dont_have_duplicate = False

    return flag_dont_have_duplicate

def search_zero(matrix, n):
    flag_dont_have_zero = True

    for i in matrix:
        if i.count(0) != 0:
            flag_dont_have_zero = False

    return flag_dont_have_zero

def definition_magic_square(matrix, n):
    need_num = sum(matrix[0])
    flag_magic_square = True

    # проверка горизонтальных линий
    for hor_line in matrix:
        if sum(hor_line) != need_num:
            flag_magic_square = False

    # проверка вертикальных линий
    for i in range(n):
        sum_vert_line = 0
        for j in range(n):
            sum_vert_line += matrix[j][i]

        if sum_vert_line != need_num:
            flag_magic_square = False

    # проверка главной диагонали
    sum_main_line = 0
    for i in range(n):
        sum_main_line += matrix[i][i]

    if sum_main_line != need_num:
        flag_magic_square = False

    # проверка побочной диагонали
    sum_side_line = 0
    for i in range(n):
        sum_side_line += matrix[i][n - i - 1]

    if sum_side_line != need_num:
        flag_magic_square = False

    if not search_duplicate(matrix, n):
        flag_magic_square = False

    if not search_zero(matrix, n):
        flag_magic_square = False

    return flag_magic_square


n = int(input())
matrix = []
matrix = filling_matrix(matrix, n)

print('YES' if definition_magic_square(matrix, n) else 'NO')
