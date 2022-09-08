mat_first_pl = input()
mat_second_pl = input()

win_materials = {'камень': ('ножницы', 'ящерица'), 'ножницы': ('бумага', 'ящерица'),
                 'бумага': ('камень', 'Спок'), 'ящерица': ('бумага', 'Спок'),
                 'Спок': ('ножницы', 'камень')}

if mat_first_pl == mat_second_pl:
    print('ничья')
elif mat_second_pl in win_materials[mat_first_pl]:
    print('Тимур')
else:
    print('Руслан')