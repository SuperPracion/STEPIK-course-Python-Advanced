words_dict = {}

for word in input().replace('  ', ' ').split():
    words_dict[word] = words_dict.setdefault(word, 0) + 1
    print(words_dict[word], end=' ')