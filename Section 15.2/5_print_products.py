def print_products(*args):
    products = [product for product in args if type(product) == str and product]

    if products:
        for i in range(len(products)):
            print(f'{i + 1}) {products[i]}')
    else:
        print('Нет продуктов')

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)