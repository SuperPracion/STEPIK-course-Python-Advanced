store_purchases = {}
for _ in range(int(input())):
    name, purchase, quantity = input().split()
    store_purchases.setdefault(name, {}).setdefault(purchase, 0)
    store_purchases[name][purchase] += int(quantity)

for name in sorted(store_purchases.keys()):
    print(f'{name}:')
    for lot in sorted(store_purchases[name].keys()):
        print(f'{lot} {store_purchases[name][lot]}')