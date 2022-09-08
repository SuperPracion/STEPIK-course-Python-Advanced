rus_alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
in_srt = input() + ' запретил букву'

for symbol in rus_alphavite:
    if symbol in in_srt:
        print(in_srt, symbol)
        in_srt = in_srt.replace(symbol, '').replace('  ', ' ').strip()
