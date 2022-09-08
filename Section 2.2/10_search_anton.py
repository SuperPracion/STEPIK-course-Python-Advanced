def word_search(list_str, need_word):
    for str in list_str:
        search_word = need_word
        for symbol in str:
            if search_word and symbol == search_word[0]:
                search_word = search_word.replace(symbol, '', 1)

        if search_word == '':
            print(list_str.index(str) + 1, end=' ')


mass_string = [input() for _ in range(int(input()))]
search_word = 'anton'

word_search(mass_string, search_word)
