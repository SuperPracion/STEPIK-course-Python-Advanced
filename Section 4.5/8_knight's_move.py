from math import *


def get_position(position):
    first_coord = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

    return [8 - int(position[1]), first_coord[position[0]]]


def filling_game_table(chessboard_size):
    chessboard = []
    for _ in range(chessboard_size):
        chessboard.append(['.' for _ in range(chessboard_size)])

    return chessboard


def search_moves(chessboard, f_chess_poss, s_chess_poss):
    n = len(chessboard)
    for i in range(n):
        for j in range(n):
            if abs((i - f_chess_poss) * (j - s_chess_poss)) == 2:
                chessboard[i][j] = '*'

    return chessboard


position_list = get_position(input())
game_table = filling_game_table(8)
game_table = search_moves(game_table, position_list[0], position_list[1])

game_table[position_list[0]][position_list[1]] = 'N'

for i in range(len(game_table)):
    for j in range(len(game_table)):
        print(game_table[i][j], end=' ')
    print()
