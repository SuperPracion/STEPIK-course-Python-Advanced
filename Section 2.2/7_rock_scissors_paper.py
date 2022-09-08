material_firs_pl = input()
material_second_pl = input()

win_materials = {'камень': 'ножницы', 'ножницы': 'бумага', 'бумага': 'камень'}

if material_firs_pl == material_second_pl:
    print('ничья')
elif win_materials[material_firs_pl] == material_second_pl:
    print('Тимур')
else:
    print('Руслан')