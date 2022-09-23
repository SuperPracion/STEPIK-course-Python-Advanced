dict_num_str_value = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 0: 'zero'}
in_num = tuple(input())

for num in in_num:
    print(dict_num_str_value[int(num)], end=' ')