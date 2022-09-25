secret_str = [symbol for symbol in input()]
decryption_dict = {}

for _ in range(int(input())):
    letter, number = input().replace(':', '').split()
    replaced_char = [symbol for symbol in secret_str if secret_str.count(symbol) == int(number)][0]
    for symbol in secret_str:
        if symbol == replaced_char:
            secret_str[secret_str.index(symbol)] = letter

print(''.join(secret_str))