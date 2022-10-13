with open('ledger.txt', 'rt', encoding='utf-8') as file:
    print(f'${sum(map(lambda x: int(x[1:]), file))}')