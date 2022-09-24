in_str = input().split()

marks = {}

for letter in in_str:
    marks.setdefault(letter, [0]).append(max(marks.get(letter, 0)) + 1)

for letter in in_str:
    if marks[letter][0]:
        print(f'{letter}_{marks[letter][0]}', end=' ')
    else:
        print(letter, end=' ')

    del marks[letter][0]