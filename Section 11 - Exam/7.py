def merge(values):  # values - это список словарей
    result_dict = {}

    for dictionary in values:
        for key, values in dictionary.items():
            result_dict.setdefault(key, set()).add(values)

    return result_dict


print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))
