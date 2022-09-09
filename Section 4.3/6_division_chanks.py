def div_into_chunks(str, need_len_str):
    mass = [[]]

    for symbol in str:
        if len(mass[-1]) < need_len_str:
            mass[-1].append(symbol)
        else:
            mass.append([symbol])

    return mass


str = input().split()
n = int(input())

print(div_into_chunks(str, n))
