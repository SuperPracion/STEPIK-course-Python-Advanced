telephone_book = {}

for _ in range(int(input())):
    number, name = input().lower().split()
    telephone_book.setdefault(name, []).append(number)

for _ in range(int(input())):
    print(*telephone_book.get(input().lower(), ['абонент не найден']))