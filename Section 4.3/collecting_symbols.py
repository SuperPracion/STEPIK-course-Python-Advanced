def search_index_complex(mass, symbol):
    index = -1

    for collection in mass:
        if symbol in collection:
            index = mass.index(collection)

    return index


def zip_duplicates(string):
    gen_mass = []

    for symbol in string:
        index_collection = search_index_complex(gen_mass, symbol)

        if index_collection == -1:
            gen_mass.append([symbol])
        else:
            gen_mass[index_collection].append(symbol)

    return gen_mass


gen_str = input().replace(' ', '')
print(zip_duplicates(gen_str))