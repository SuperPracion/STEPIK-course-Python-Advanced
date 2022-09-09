def collecting(string):
    gen_mass = []

    for symbol in string:
        if gen_mass and symbol in gen_mass[-1]:
            gen_mass[-1].append(symbol)
        else:
            gen_mass.append([symbol])

    return gen_mass

gen_str = input().replace(' ', '')
print(collecting(gen_str))