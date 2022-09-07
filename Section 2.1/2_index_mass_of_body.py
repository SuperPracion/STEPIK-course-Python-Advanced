mass_body = float(input())
hight_body = float(input())
IMB = (mass_body) / (hight_body * hight_body)

if 18.5 <= IMB <= 25:
    print('Оптимальная масса')
elif 18.5 > IMB:
    print('Недостаточная масса')
else:
    print('Избыточная масса')