import string
from random import *


def generate_password(length):
    password_components = string.ascii_letters + string.digits
    return sample(password_components, length)


def generate_passwords(count, lenght):
    passwords = []
    while len(passwords) != count:
        temp_pass = generate_password(lenght)
        if sum([1 for item in temp_pass if item in ['l', 'I', '1', '0', 'o', 'O']]) == 0:
            passwords.append(''.join(temp_pass))

    return passwords


count, lenght = [int(input()) for _ in range(2)]
passwords = generate_passwords(count, lenght)
print(*passwords, sep='\n')