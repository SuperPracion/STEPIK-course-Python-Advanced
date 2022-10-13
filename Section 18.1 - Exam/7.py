with open('cyrillic.txt', 'rt', encoding='utf-8') as file, open('transliteration.txt', 'w', encoding='utf-8') as output_text:
    translation_lower = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'jo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
                   'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shh', 'ъ': '*', 'ы': 'y', 'ь': '\'',
                   'э': 'je', 'ю': 'ju', 'я': 'ya'}

    translation_upper = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Jo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'J', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
                         'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C',
                         'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shh', 'Ъ': '*', 'Ы': 'Y', 'Ь': '\'', 'Э': 'Je', 'Ю': 'Ju', 'Я': 'Ya'}

    content = file.read()
    for letter in content:
        print_letter = letter
        if letter in translation_lower:
            print_letter = translation_lower[letter]
        elif letter in translation_upper:
            print_letter = translation_upper[letter]

        print(print_letter, end='', file=output_text)