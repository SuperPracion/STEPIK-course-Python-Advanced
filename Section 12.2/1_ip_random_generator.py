from random import *


def generate_ip():
    ip_address = [str(randint(0, 255)) for _ in range(4)]
    return '.'.join(ip_address)


print(generate_ip())
