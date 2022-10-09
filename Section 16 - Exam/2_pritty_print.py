def pretty_print(data, side='-', delimiter='|'):
    new_data = f' {delimiter} '.join(map(str, data))

    print('', f'{side}' * (len(new_data) + 2))
    print(f'{delimiter} {new_data} {delimiter}')
    print('', f'{side}' * (len(new_data) + 2))


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')