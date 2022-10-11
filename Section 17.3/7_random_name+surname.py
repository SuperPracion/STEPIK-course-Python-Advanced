import random

with open('first_names.txt', 'r', encoding='utf-8') as names, open('last_names.txt', 'r', encoding='utf-8') as last_name:
    list_names = names.readlines()
    list_last_names = last_name.readlines()
    for _ in range(3):
        print(random.choice(list_names).strip(), random.choice(list_last_names).strip())