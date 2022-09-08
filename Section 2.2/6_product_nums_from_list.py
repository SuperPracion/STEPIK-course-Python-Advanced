mass_num = [int(input()) for _ in range(int(input()))]
search_product = int(input())
flag_number_is = False

for i in range(len(mass_num)):
    for j in range(len(mass_num)):
        if i != j and mass_num[i] * mass_num[j] == search_product:
            flag_number_is = True

print('ДА' if flag_number_is else 'НЕТ')
